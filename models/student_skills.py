from odoo import api, fields, models


class Skill(models.Model):
    _name = 'skill'

    name = fields.Char(string="Name")


class StudentSkillHistory(models.Model):
    _name = 'student.skill.history'
    _inherit = 'student.skill'

    comment = fields.Text(string="Comment")

