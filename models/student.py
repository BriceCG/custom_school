from odoo import api, fields, models
import numpy as np


class Student(models.Model):
    _name = 'school.student'

    name = fields.Char(string="Name")
    first_name = fields.Char(string="First Name")

    age = fields.Char(string="Age")
    date_of_birth = fields.Date(string="Date of birth")

    image = fields.Binary(string="Image")
    address = fields.Char(string="Addess")
    phone = fields.Char(string="Phone")
    email = fields.Char(string="Email")
    school_id = fields.Many2one('student.school')

    experience_ids = fields.One2many('student.experience', 'student_id')

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