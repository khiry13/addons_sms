from odoo import models, fields, api


class Student(models.Model):

    # region ---------------------- TODO[IMP]: Private Attributes --------------------------------
    _name = "sms_module.student"
    _description = "Student"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _sql_constraints = [
        ('unique_student_name', 'unique("name")', 'Student name is exist'),
        ('unique_student_id', 'unique("student_id")', 'Student id is exist'),
    ]
    # endregion

    # region ---------------------- TODO[IMP]:Default Methods ------------------------------------
    # endregion

    # region ---------------------- TODO[IMP]: Fields Declaration ---------------------------------
    # region  Basic
    name = fields.Char()
    description = fields.Html(string='Description')
    date_of_birth = fields.Date()
    contact_details = fields.Char()
    address = fields.Char()
    guardian_details = fields.Char()
    student_id = fields.Char()
    national_doc = fields.Binary()
    image = fields.Image()
    # endregion

    # region  Special
    # endregion

    # region  Relational
    # endregion

    # region  Computed
    # endregion

    # endregion
    # region ---------------------- TODO[IMP]: Compute methods ------------------------------------
    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None, order='name asc'):
        args = args or []
        domain = ['|', ('name', operator, name), ('student_id', operator, name)]
        return self._search(domain + args, limit=limit, access_rights_uid=name_get_uid, order=order)
    # endregion

    # region ---------------------- TODO[IMP]: Constrains and Onchanges ---------------------------

    # endregion

    # region ---------------------- TODO[IMP]: CRUD Methods -------------------------------------
    # endregion

    # region ---------------------- TODO[IMP]: Action Methods -------------------------------------
    # endregion

    # region ---------------------- TODO[IMP]: Business Methods -------------------------------------
    # endregion