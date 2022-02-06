from odoo import api, fields, models
from odoo.exceptions import ValidationError
import numpy as np


class Student(models.Model):
    _name = 'school.student'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Name")
    first_name = fields.Char(string="First Name")

    age = fields.Char(string="Age")
    date_of_birth = fields.Date(string="Date of birth")

    image = fields.Binary(string="Image")
    address = fields.Char(string="Addess")
    phone = fields.Char(string="Phone")
    email = fields.Char(string="Email")
    school_id = fields.Many2one('student.school')
    faculty_id = fields.Many2one('student.faculty', string="Faculty")

    experience_ids = fields.One2many('student.experience', 'student_id')
    skill_ids = fields.One2many('student.skill', 'student_id')

    def print_student(self):
        return self.env.ref('custom_school.action_student_report_card').report_action(None, data=None)


class StudentExperience(models.Model):
    _name = 'student.experience'

    student_id = fields.Many2one('school.student', string="Student")
    date_from = fields.Date(string="Date from")
    date_to = fields.Date(string="Date to")
    student_company_id = fields.Many2one('student.company', string="Company")
    duration = fields.Float(string="Duration(days)", compute='_compute_duration', store=True)

    @api.depends('date_to', 'date_from')
    def _compute_duration(self):
        for rec in self:
            if rec.date_to and rec.date_from:
                rec.duration = np.busday_count(rec.date_from, rec.date_to)
            else:
                rec.duration = 0


class StudentSkillLine(models.Model):
    _name = 'student.skill'

    student_id = fields.Many2one('school.student')
    skill_id = fields.Many2one('skill', string="Skill")
    school_id = fields.Many2one('student.school', related='student_id.school_id', store=True)
    skill_search_id = fields.Many2one('skill', string="Skill")
    rate_number = fields.Float(string="Rate number")
    rating = fields.Selection([
        ('firts', 'first'),
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ], compute='_compute_rating', store=True)

    @api.depends('rate_number')
    def _compute_rating(self):
        for rec in self:
            if rec.rate_number != 0:
                if rec.rate_number < 5:
                    rec.rating = 'low'
                elif 5 <= rec.rate_number < 8:
                    rec.rating = 'medium'
                elif rec.rate_number >= 8:
                    rec.rating = 'high'
            else:
                rec.rating = None

    @api.constrains('rate_number')
    def rate_number_constraints(self):
        for rec in self:
            if rec.rate_number > 10:
                raise ValidationError('The rate cannot be superior to 10')


class ReportStudent(models.AbstractModel):
    _name = 'report.custom_school.school_report'

    @api.model
    def _get_report_values(self, docids, data=None):
        data = {
            'date_from': 'test'
        }
        docs = self.env['school.student'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'school.student',
            'docs': docs,
            'data': data,
            'get_something': self.get_something,
        }

    def get_something(self):
        return 5