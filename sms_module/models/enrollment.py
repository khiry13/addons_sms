from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Enrollment(models.Model):

    # region ---------------------- TODO[IMP]: Private Attributes --------------------------------
    _name = "sms_module.enrollment"
    _description = "Enrollment"
    _sql_constraints = [
        ('unique_student_course', 'unique(student_id, course_id)',
         'The combination of student and course must be unique!')
    ]
    # endregion

    # region ---------------------- TODO[IMP]:Default Methods ------------------------------------
    # endregion

    # region ---------------------- TODO[IMP]: Fields Declaration ---------------------------------
    # region  Basic
    enrollment_date = fields.Date()
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ], default='draft')
    course_name = fields.Char(related='course_id.name', store=True)
    course_duration = fields.Integer()
    # endregion

    # region  Special
    # endregion

    # region  Relational
    student_id = fields.Many2one('sms_module.student', domain="[('activate', '=', True)]")
    course_id = fields.Many2one('sms_module.course')
    # endregion

    # region  Computed
    # endregion

    # endregion
    # region ---------------------- TODO[IMP]: Compute methods ------------------------------------
    # endregion

    # region ---------------------- TODO[IMP]: Constrains and Onchanges ---------------------------
    @api.onchange('course_id')
    def _onchange_course_id(self):
        if self.course_id:
            self.course_duration = self.course_id.course_duration
        else:
            self.course_duration = 0

    @api.constrains('enrollment_date')
    def _check_enrollment_date(self):
        for record in self:
            if record.enrollment_date and record.enrollment_date > fields.Date.today():
                raise ValidationError("The enrollment date cannot be in the future.")
    # endregion

    # region ---------------------- TODO[IMP]: CRUD Methods -------------------------------------
    # endregion

    # region ---------------------- TODO[IMP]: Action Methods -------------------------------------
    # endregion

    # region ---------------------- TODO[IMP]: Business Methods -------------------------------------
    # endregion