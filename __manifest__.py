# -*- coding: utf-8 -*-
{
    'name': "sidebar_plugin",

    'summary': """
       增加左侧常驻菜单""",

    'description': """
        继承nav视图的QWEB，重写模板和视图
    """,

    'author': "Mr.Yang",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'application',
    "application" :  True,
    'version': '0.1',

    # any module necessary for this one to work correctly
    "depends": [
        'web',
    ],

    # always loaded
    'data': [
        'views/assets.xml',
        'views/sidebar.xml',
    ],
    'qweb': [
        'static/src/xml/menu_inherit.xml'
    ]
}