from odoo import models, fields

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
    attendance_date = fields.Date()
    status = fields.Char()
    # endregion

    # region  Special
    # endregion

    # region  Relational
    student_id = fields.Many2one('sms_module.student')
    course_id = fields.Many2one('sms_module.course')
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
    # endregion