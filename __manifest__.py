# -*- coding: utf-8 -*-
{
    'name': "Bajaagung",

    'summary': """
        Aplikasi Baja Agung""",

    'description': """
        Aplikasi Baja Agung
    """,

    'author': "Eries Herman",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','purchase','stock'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
        'views/product_template_only_form_view.xml',
        'views/unit_of_measure_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}