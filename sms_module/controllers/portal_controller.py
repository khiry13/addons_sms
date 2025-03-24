from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal

class CustomPortal(CustomerPortal):
    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        if 'portal_student_course' in counters:
            values['portal_student_course'] = request.env[
                'sms_module.student'].sudo().search_count([])
        return values

    @http.route(['/student_course', '/student_course/page/<int:page>'], type='http', auth="user", website=True)
    def portal_student_course(self, search=None, search_in='All', filterby='All', groupby='none'):

        searchbar_inputs = {
            'All': {'label': 'All', 'input': 'All', 'domain': []},
            'Student Name': {'label': 'Student Name', 'input': 'Student Name', 'domain': [('name', 'like', search)]},
            'Course': {'label': 'Course', 'input': 'Course', 'domain': [('course_name', 'like', search)]},
        }
        # Define the search bar filters
        searchbar_filters = {
            'All': {'label': 'All', 'domain': []},
            'Active': {'label': 'Active', 'domain': [('status', '=', 'Active')]},
            'Completed': {'label': 'Completed', 'domain': [('status', '=', 'Completed')]},
        }
        search_domain = searchbar_inputs[search_in]['domain']
        filter_domain = searchbar_filters.get(filterby, searchbar_filters['All'])['domain']
        combined_domain = search_domain + filter_domain
        student_course = request.env['sms_module.student'].sudo().search([
            ('student_id', '=', request.env.user.partner_id.id)])
        search_student_course = student_course.search(combined_domain)
        return request.render('sms_module.portal_my_home_student_course_views',
                              {
                                  'student_course': search_student_course,
                                  'page_name': 'student_course',
                                  'search': search,
                                  'search_in': search_in,
                                  'searchbar_inputs': searchbar_inputs,
                                  'filterby': filterby,
                                  'searchbar_filters': searchbar_filters,
                                  'default_url': '/student_course',
                              })