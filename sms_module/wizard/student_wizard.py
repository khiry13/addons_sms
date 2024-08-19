from odoo import models, fields, api


class StudentWizard(models.TransientModel):
    _name = 'sms_module.student_wizard'
    _description = 'Wizard for Students Interests'

    student_ids = fields.Many2many('sms_module.student', string='Interests')
