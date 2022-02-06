from odoo import api, fields, models


class Skill(models.Model):
    _name = 'skill'

    name = fields.Char(string="Name")

    