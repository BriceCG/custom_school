from odoo import api, fields, models


class StudentFaculty(models.Model):
    _name = 'student.faculty'
    _description = 'Filliere'

    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
    school_id = fields.Many2one('student.school')
    category = fields.Selection([
        ('science', 'Science'),
        ('marketing', 'Marketing'),
        ('communication', 'Communication'),
        ('management', 'Management'),
        ('computer_science', 'Computer Science')
    ])