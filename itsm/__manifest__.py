# -*- coding: utf-8 -*-
{
    'name': "IT Services Management",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Ridwan Aden",
    'website': "http://www.rootkits.id",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail','board'],

    # always loaded
    'data': [
        'report/report_action.xml',
        'report/report_asset_assign.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/dashboard.xml',
        'views/asset.xml',
        'views/credential.xml',
        'views/services.xml',
        'views/assign.xml',
        'views/renewal.xml',
        'views/reporting.xml',
        'views/category.xml',
        'views/brands.xml',
        'views/location.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
