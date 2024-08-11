from odoo import models, fields


class EmergencyContact(models.Model):
    _name = 'sms_module.emergency_contact'
    _inherits = {'res.partner': 'partner_id'}

    partner_id = fields.Many2one('res.partner', required=True, ondelete="cascade")
    student_id = fields.Char(string='Student ID')
    contact_type = fields.Selection([
        ('emergency', 'Emergency'),
        ('alternate', 'Alternate')
    ], string='Contact Type', required=True)
