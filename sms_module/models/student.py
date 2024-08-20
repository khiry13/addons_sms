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
    name = fields.Char(tracking=True)
    description = fields.Html(string='Description')
    date_of_birth = fields.Date()
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], default='male')
    contact_details = fields.Char(tracking=True)
    address = fields.Char()
    guardian_details = fields.Char()
    student_id = fields.Char(string='Student ID', required=True, copy=False, readonly=True, index=True, default=lambda self: ('New'))
    national_doc = fields.Binary()
    image = fields.Image()
    activate = fields.Boolean(default=True)
    active = fields.Boolean(default=True)
    attendance_percentage = fields.Float()
    priority = fields.Integer()
    priority_level = fields.Selection([
            ('0', 'Normal'),
            ('1', 'Low'),
            ('2', 'Medium'),
            ('3', 'High')
    ])
    submit_evaluation = fields.Boolean(string="Submit Evaluation", default=False)
    profile_link = fields.Char(help="URL of the student's profile")
    mood_feedback = fields.Char(help="Visual feedback on student moods using emojis")

    # endregion

    # region  Special
    # endregion

    # region  Relational
    enrollment_ids = fields.One2many('sms_module.enrollment', 'student_id', string='Enrollments')
    grade_ids = fields.One2many('sms_module.grade', 'student_id', string='Grades')
    attendance_ids = fields.One2many('sms_module.attendance', 'student_id', string='Attendences')
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

    @api.depends('name', 'student_id')
    def _compute_display_name(self):
        for record in self:
            if self.env.context.get('display_id'):
                record.display_name = f'[{record.student_id}] {record.name}'
            else:
                record.display_name = record.name
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

    def action_trigger_students_age(self):
        age_threshold = 18
        adult_students = self.with_context(age_threshold=age_threshold).get_adult_students()
        # Display the filtered students in a popup view (e.g., a tree view)
        return {
            'name': 'Adult Students',
            'type': 'ir.actions.act_window',
            'res_model': 'sms_module.student',
            'view_mode': 'tree',
            'target': 'new',
            'domain': [('id', 'in', adult_students.ids)],
        }

    @api.model
    def submit_student_evaluation(self):
        for record in self:
            if not record.submit_evaluation:

                record.submit_evaluation = True
    # endregion

    # region ---------------------- TODO[IMP]: Business Methods -------------------------------------
    def open_url(self):
        url = 'https://www.google.com'  # Replace with your desired URL
        return {
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': url,
        }

    def get_adult_students(self):
        age_threshold = self.env.context.get('age_threshold')
        adult_students = self.search([('age', '>=', age_threshold)])
        return adult_students

    def open_student_wizard(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Select Interests',
            'res_model': 'sms_module.student_wizard',
            'view_mode': 'form',
            'target': 'new',
        }
    # endregion


