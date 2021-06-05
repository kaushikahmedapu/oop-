from odoo import models,fields,api, _

class Test(models.Model):
    _name = "test.requisition"
    _description = "test"
    


    name = fields.Char(string='NAME')