# -*- coding: utf-8 -*-
{
    'name': "Modificaciones Formulario de Contacto",

    'summary': """
        Modificaciones al formulario de contacto para uso general e interno""",

    'description': """
        Este módulo agrega los campos de 
        
        -advance_payment_date
        -percent_supplier_advance
        -lt_ag_channel
    """,

    'author': "Wonderbrands",
    'website': "https://www.wonderbrands.co",
    'license': 'LGPL-3',

    'category': 'Inventory',
    'version': '15.0',

    # any module necessary for this one to work correctly
    'depends': ['base',
                'contacts',],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/partner_fields_form_view.xml',
    ],
}
