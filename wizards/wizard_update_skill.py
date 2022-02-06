from odoo import api, fields, models


class UpdateSkill(models.TransientModel):
    _name = 'wizard.update.skill'

    date = fields.Date(string="Date", default=fields.Date.today())
    comment = fields.Text(string="Comment")
    rate_number = fields.Float(string="Rate Number")

    def update_skill(self):
        student_skill_id = self.env['student.skill'].browse(self._context.get('active_id'))
        # Create new skill history
        self.env['student.skill.history'].create({
            'date': student_skill_id.date,
            'rate_number': student_skill_id.rate_number,
            'skill_id': student_skill_id.skill_id.id,
            'student_id': student_skill_id.student_id.id
        })

        # Update the current skill
        student_skill_id.rate_number = self.rate_number
        student_skill_id.date = self.date

        pass