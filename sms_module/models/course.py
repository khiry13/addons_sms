from odoo import models, fields

class Course(models.Model):

    # region ---------------------- TODO[IMP]: Private Attributes --------------------------------
    _name = "sms_module.course"
    _description = "Course"
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
    # endregion

    # region  Special
    # endregion

    # region  Relational
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