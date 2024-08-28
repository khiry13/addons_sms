from datetime import timedelta

from odoo import models, fields, api
from odoo import _, exceptions
from odoo.exceptions import ValidationError


class Enrollment(models.Model):

    # region ---------------------- TODO[IMP]: Private Attributes --------------------------------
    _name = "sms_module.enrollment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
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
    ], default='draft', tracking=True)
    course_name = fields.Char(related='course_id.name', store=True)
    course_duration = fields.Integer()
    # endregion

    # region  Special
    # endregion

    # region  Relational
    student_id = fields.Many2one('sms_module.student', domain="[('activate', '=', True)]")
    course_id = fields.Many2one('sms_module.course')
    teacher_id = fields.Many2one('res.users', string="Teacher", required=True)

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
                raise exceptions.ValidationError(_("The enrollment date cannot be in the future."))
    # endregion

    # region ---------------------- TODO[IMP]: CRUD Methods -------------------------------------
    @api.model
    def create(self, vals):
        res = super(Enrollment, self).create(vals)
        student = res.student_id
        course = res.course_id

        message = f"Student '{student.name}' has been enrolled in the course '{course.name}' on {res.enrollment_date}."

        student.message_post(body=message)

        res.schedule_enrollment_notification()

        return res
    # endregion

    # region ---------------------- TODO[IMP]: Action Methods -------------------------------------
    # endregion

    # region ---------------------- TODO[IMP]: Business Methods -------------------------------------
    def schedule_enrollment_notification(self):
        """Schedules a notification activity for the teacher about the new enrollment."""
        if self.teacher_id:
            # Calculate the notification deadline (enrollment_date + 2 days)
            notification_deadline = fields.Date.from_string(self.enrollment_date) + timedelta(days=2)

            # Schedule an activity for the teacher
            self.activity_schedule(
                'mail.mail_activity_data_todo',  # Activity type: To Do
                date_deadline=notification_deadline,
                user_id=self.teacher_id.id,
                summary=_("New student enrollment confirmed: %s") % (self.student_id.name)
            )

    # endregion