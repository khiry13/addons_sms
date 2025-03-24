# -*- coding: utf-8 -*-
{
    'name': "sms_module",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', 'sale', 'web', 'calendar'],

    # always loaded
    'data': [
        'security/groups.xml',
        'security/security.xml',
        'security/ir.model.access.csv',

        'data/student_sequence.xml',
        # 'data/cron_job_data.xml',

        'views/student_views.xml',
        'views/course_views.xml',
        'views/enrollment_views.xml',
        'views/grade_views.xml',
        'views/attendance_views.xml',
        'views/res_partner_views.xml',
        'views/extended_course_views.xml',
        'views/emergency_contact_views.xml',
        'views/sms_config_settings_views.xml',
        'views/dashboard_action.xml',
        'views/student_course_portal.xml',
        'views/menus.xml',

        'reports/student_report.xml',

        'demo/demo_data.xml',

        'wizard/make_enroll_wizard_views.xml',
        'wizard/student_wizard_views.xml',
        'wizard/select_record_wizard_views.xml'

        # 'views/views.xml',
        # 'views/templates.xml',
    ],
    'controllers': [
    'controllers/portal_controller.py',
    ],
    'assets': {
        'web.assets_backend': [
            'sms_module/static/src/scss/dashboard.scss',
            'sms_module/static/src/js/age_field_widget.js',
            'sms_module/static/src/xml/age_field_widget.xml',
            'sms_module/static/src/xml/dashboard_count_item.xml',
            'sms_module/static/src/js/dashboard_count_item.js',
            'sms_module/static/src/js/dashboard.js',
            'sms_module/static/src/xml/dashboard_template.xml',
    #
        ],
    },
        # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}
