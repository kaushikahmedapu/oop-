from odoo import models, fields, api
import calendar

class SalesDescription(models.Model):
    _inherit = 'product.template'
    
    dealer_ids = fields.Many2one('dealer.addon',string='Dealer Name')
    product_ids = fields.Many2one('product.addon',string='Product Brand')
    
