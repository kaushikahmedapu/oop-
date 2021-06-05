from odoo import fields, models

class UniStaffInherit(models.Model):
    _inherit = 'res.partner'

    fax = fields.Char(string='Fax')