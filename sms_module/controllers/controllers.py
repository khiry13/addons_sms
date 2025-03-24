from odoo import http
from odoo.http import request


class DashboardController(http.Controller):

    @http.route('/sms_module/dashboard/data', type='json', auth='user')
    def get_dashboard_data(self):
        # Fetch dynamic data from the server
        user_count = request.env['res.users'].search_count([])
        student_count = request.env['sms_module.student'].search_count([])
        alerts_count = request.env['mail.activity'].search_count([])
        orders_count = request.env['sale.order'].search_count([])

        return {
            'user_count': user_count,
            'student_count': student_count,
            'alerts_count': alerts_count,
            'orders_count': orders_count,
        }
