# -*- coding: utf-8 -*-
{
    'name': "custom_club",

    'summary': "Custom Club",

    'description': """
    
        Ajouter un nouveau champs : “Club Or” (oui/non) sur le partner et l’afficher dans la
        vue formulaire, dans l’onglet Sales & Purchase sous le champs Pricelist
    """,

    'author': "Arche TI",
    'website': "https://www.archeti.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales/Sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [],
    # only loaded in demonstration mode
    'demo': [],
}
