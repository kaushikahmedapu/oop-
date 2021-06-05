from odoo import models,fields,api, _
from datetime import datetime
from odoo.exceptions import UserError



class WardBoy(models.Model):
    _name = "wardboy.addon"
    _description = "test"
    


    name = fields.Char(string='NAME')
    # lname = fields.Char(string='LAST NAME')
    # name = fields.Char(string="NAME", compute="_get_full_name" )
    id_card = fields.Integer(string="ID CARD")
    ward_num = fields.Char(string="ROOM NUMBER")
    # code = fields.Char(string='CODE')
    age = fields.Integer(string= "AGE")
    ward_boy_address = fields.Text(string="ward Boy Address")
    ward_boy_photo = fields.Binary(string="ward Boy Photo", attachment=True)
    date_of_birth = fields.Date(
                string='Date of birth', default=datetime.today())
    
    
