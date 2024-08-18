from datetime import datetime, date

from odoo import models, fields, api


class Attendance(models.Model):

    # region ---------------------- TODO[IMP]: Private Attributes --------------------------------
    _name = "sms_module.attendance"
    _description = "Attendance"
    _sql_constraints = [
        ('unique_attendance', 'unique(attendance_date, student_id, course_id)',
         'The combination of attendance date, student, and course must be unique!')
    ]
    # endregion

    # region ---------------------- TODO[IMP]:Default Methods ------------------------------------
    # endregion

    # region ---------------------- TODO[IMP]: Fields Declaration ---------------------------------
    # region  Basic
    attendance_date = fields.Date(default=lambda self: self._default_attendance_date())
    status = fields.Char()
    absence_notes = fields.Text()
    comments = fields.Text()
    class_name = fields.Char()
    internal_notes = fields.Text()
    checkin_time = fields.Datetime(default=lambda self: self._default_checkin_time())
    # endregion

    # region  Special
    # endregion

    # region  Relational
    student_id = fields.Many2one('sms_module.student')
    course_id = fields.Many2one('sms_module.course')
    teacher_id = fields.Many2one('res.users', string="Teacher", required=True)
    # endregion

    # region  Computed
    # endregion

    # endregion
    # region ---------------------- TODO[IMP]: Compute methods ------------------------------------
    # endregion

    # region ---------------------- TODO[IMP]: Constrains and Onchanges ---------------------------

    # endregion

    # region ---------------------- TODO[IMP]: CRUD Methods -------------------------------------
    # endregion

    # region ---------------------- TODO[IMP]: Action Methods -------------------------------------
    # endregion

    # region ---------------------- TODO[IMP]: Business Methods -------------------------------------
    @api.model
    def _default_attendance_date(self):
        return date.today()

    @api.model
    def _default_checkin_time(self):
        return datetime.now()

    @api.model
    def update_student_attendance_status(self):
        today = fields.Date.today()
        records = self.search([('attendance_date', '=', today), ('status', 'not in', ['present', 'absent'])])
        records.write({'status': 'absent'})
    # endregion