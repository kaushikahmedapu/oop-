
{
    'name' : 'Inherited Purchase Module',
    'version' : '14.0',
    'summary': '',
    'sequence': 10,
    'description': '',
    'category': '',
    'website': 'https://www.odoo.com',
    'depends' : [
        'purchase',
        # 'product_inherit_view',

    ],
    'data': [
        'views/purchase_inherited_view.xml',
        'views/purchase_filter.xml',

    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
