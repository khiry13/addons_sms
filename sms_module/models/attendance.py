from datetime import datetime, date

from odoo import models, fields, api

import logging

_logger = logging.getLogger(__name__)


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
    is_present = fields.Boolean(string='Is Present', compute='_compute_is_present')
    # endregion

    # endregion
    # region ---------------------- TODO[IMP]: Compute methods ------------------------------------
    @api.depends('status')
    def _compute_is_present(self):
        for record in self:
            record.is_present = record.status == 'present'
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

    @api.model
    def _cron_generate_absent_records(self):
        today = fields.Date.context_today(self)
        students = self.env['sms_module.student'].search([])
        absent_count = 0
        try:
            for student in students:
                attendance = self.env['sms_module.attendance'].search([
                    ('student_id', '=', student.id),
                    ('attendance_date', '=', today)
                ])

                if not attendance:
                    self.create({
                        'student_id': student.id,
                        'attendance_date': today,
                        'status': 'absent'
                    })
                    absent_count += 1

            _logger.info(f'Cron Job: {absent_count} absent records created for unassigned students on {today}.')
        except Exception as e:
            _logger.error(f'Error in Cron Job: {e}')


    # endregion