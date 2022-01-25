from odoo import api, fields, models


class StudentCompany(models.Model):
    _name = 'student.company'

    name = fields.Char(string="Name")
    logo = fields.Binary(string="Logo")

    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    description = fields.Text(string="Description")
    website = fields.Char(string="Website")

    category = fields.Selection([
        ('digital', 'Digital'),
        ('engineering', 'Engineering'),
        ('outsourcing', 'Outsourcing'),
        ('finance', 'Finance')
    ])