from odoo import models,fields,api, _
from datetime import datetime
from odoo.exceptions import UserError



class Nurse(models.Model):
    _name = "nurse.addon"
    _description = "test"
    


    name = fields.Char(string='NAME')
    # lname = fields.Char(string='LAST NAME')
    # name = fields.Char(string="NAME", compute="_get_full_name" )
    id_card = fields.Integer(string="ID CARD")
    ward_num = fields.Char(string="ROOM NUMBER")
    # code = fields.Char(string='CODE')
    age = fields.Integer(string= "AGE")
    nurse_address = fields.Text(string="NURSE Address")
    nurse_photo = fields.Binary(string="NURSE Photo", attachment=True)
    date_of_birth = fields.Date(
                string='Date of birth', default=datetime.today())
    deauty_under_ids = fields.Many2one('doctor.addon',string="Deauty Under")
    

    @api.model
    def create(self, values):
        values['age'] = 40
        result = super(Nurse, self).create(values)
        return result

    # def write(self, values):
    #     values['age'] = 32
    #     result = super(Nurse,self).write(values)
    #     return result

    @api.onchange('age')
    def onchange_age(self):
        if self.age>15:
            self.nurse_address = "Dhaka"