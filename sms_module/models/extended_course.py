from odoo import models, fields


class ExtendedCourse(models.Model):
    _name = 'sms_module.extended_course'
    _inherit = 'sms_module.course'

    course_prerequisite = fields.Text()
