from odoo import models, fields

class SMSConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    default_course_duration = fields.Integer(
        string="Default Course Duration (days)",
        config_parameter='sms_module.default_course_duration',
        default=30,
        default_model='sms_module.course'
    )
    max_students_per_course = fields.Integer(
        string="Maximum Number of Students per Course",
        config_parameter='sms_module.max_students_per_course',
        default=50,
        default_model='sms_module.course'
    )
