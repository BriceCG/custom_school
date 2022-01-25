from odoo import api, fields, models


class StudentSchool(models.Model):
    _name = 'student.school'

    name = fields.Char(string="Name")

    logo = fields.Binary(string="Logo")

    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    description = fields.Text(string="Description")
    website = fields.Char(string="Website")
