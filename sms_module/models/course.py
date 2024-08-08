from odoo import models, fields

class Course(models.Model):

    # region ---------------------- TODO[IMP]: Private Attributes --------------------------------
    _name = "sms_module.course"
    _description = "Course"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _sql_constraints = [
        ('unique_course_name', 'unique("name")', 'This name is exist'),
    ]
    # endregion

    # region ---------------------- TODO[IMP]:Default Methods ------------------------------------
    # endregion

    # region ---------------------- TODO[IMP]: Fields Declaration ---------------------------------
    # region  Basic
    name = fields.Char()
    description = fields.Char()
    syllabus = fields.Char()
    duration = fields.Integer()
    prerequisites = fields.Char()
    is_featured = fields.Boolean()
    # endregion

    # region  Special
    # endregion

    # region  Relational
    enrollment_ids = fields.One2many('sms_module.enrollment', 'course_id')
    # endregion

    # region  Computed
    number_of_enrollments = fields.Integer(compute='_compute_number_of_enrollments')
    # endregion

    # endregion
    # region ---------------------- TODO[IMP]: Compute methods ------------------------------------
    def _compute_number_of_enrollments(self):
        for record in self:
            record.number_of_enrollments = len(record.enrollment_ids)
    # endregion

    # region ---------------------- TODO[IMP]: Constrains and Onchanges ---------------------------

    # endregion

    # region ---------------------- TODO[IMP]: CRUD Methods -------------------------------------
    # endregion

    # region ---------------------- TODO[IMP]: Action Methods -------------------------------------
    def action_view_enrollments(self):
        action = self.env.ref('sms_module.enrollment_action').read()[0]
        action['domain'] = [('course_id', '=', self.id)]
        return action
    # endregion

    # region ---------------------- TODO[IMP]: Business Methods -------------------------------------
    # endregion