from datetime import datetime, date

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
    student_id = fields.Char(string='Student ID', required=True, copy=False, readonly=True, index=True, default=lambda self: ('New'))
    national_doc = fields.Binary()
    image = fields.Image()
    activate = fields.Boolean(default=True)
    active = fields.Boolean(default=True)
    # endregion

    # region  Special
    # endregion

    # region  Relational
    enrollment_ids = fields.One2many('sms_module.enrollment', 'student_id', string='Enrollments')
    # endregion

    # region  Computed
    age = fields.Integer(compute='_compute_age', store=True)
    # endregion

    # endregion
    # region ---------------------- TODO[IMP]: Compute methods ------------------------------------
    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None, order='name asc'):
        args = args or []
        domain = ['|', ('name', operator, name), ('student_id', operator, name)]
        return self._search(domain + args, limit=limit, access_rights_uid=name_get_uid, order=order)

    @api.model
    def create(self, vals):
        if vals.get('student_id', ('New')) == ('New'):
            vals['student_id'] = self.env['ir.sequence'].next_by_code('sms_module.student') or ('New')
        return super(Student, self).create(vals)

    @api.depends('date_of_birth')
    def _compute_age(self):
        for record in self:
            if record.date_of_birth:
                today = date.today()
                birth_date = fields.Date.from_string(record.date_of_birth)
                record.age = today.year - birth_date.year - (
                        (today.month, today.day) < (birth_date.month, birth_date.day)
                )
            else:
                record.age = 0
    # endregion

    # region ---------------------- TODO[IMP]: Constrains and Onchanges ---------------------------

    # endregion

    # region ---------------------- TODO[IMP]: CRUD Methods -------------------------------------
    # endregion

    # region ---------------------- TODO[IMP]: Action Methods -------------------------------------
    def action_generate_attendance_today(self):
        for student in self:
            self.env['sms_module.attendance'].create({
                'student_id': student.id,
                'attendance_date': datetime.today().date(),
                'status': 'present',
            })


    # endregion

    # region ---------------------- TODO[IMP]: Business Methods -------------------------------------
    def open_url(self):
        url = 'https://www.google.com'  # Replace with your desired URL
        return {
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': url,
        }
    # endregion


