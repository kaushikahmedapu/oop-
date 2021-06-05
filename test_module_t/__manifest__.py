{
    'name' : "Test",
    'version' :'1.0',
    'sequence' : 1,
    'website': 'https://www.odoo.com',
    'summary': 'For test purpose',
    'description' : "xyz",
    'depends' : [],
    'data' :[
        'security/test_security.xml',
        'security/ir.model.access.csv',
        'views/test.xml',
    ],
    'installable' : True,
    'application' : True,
    'auto_install' : False,
}
