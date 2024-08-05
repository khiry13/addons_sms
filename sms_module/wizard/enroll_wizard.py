from odoo import models, fields, api


class EnrollWizard(models.TransientModel):
    _name = 'enroll.wizard'
    _description = 'Wizard for Enrolling Students'

    student_ids = fields.Many2many('sms_module.student', string='Students')
    course_id = fields.Many2one('sms_module.course', string='Course', required=True)

    def action_enroll_students(self):
        Enrollment = self.env['sms_module.enrollment']
        for student in self.student_ids:
            Enrollment.create({
                'student_id': student.id,
                'course_id': self.course_id.id,
                'enrollment_date': fields.Date.today()
            })
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Success',
                'message': 'Students have been enrolled successfully.',
                'sticky': False,
            }
        }
