from odoo import models, fields, api
from odoo.exceptions import UserError


class ProductInfo(models.Model):
    _name = 'product.addon'
    _description = 'Product Info'
    

    name = fields.Char(string='Product Name')