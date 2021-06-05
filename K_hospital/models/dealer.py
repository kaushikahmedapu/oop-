from odoo import models, fields, api
from odoo.exceptions import UserError


class DealerInfo(models.Model):
    _name = 'dealer.addon'
    _description = 'Dealer Info'
    

    name = fields.Char(string='Dealer Name')