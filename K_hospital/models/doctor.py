from odoo import models,fields,api, _
from datetime import datetime
from odoo.exceptions import UserError



class Doctor(models.Model):
    _name = "doctor.addon"
    _description = "test"
    


    name = fields.Char(string='NAME')
    # lname = fields.Char(string='LAST NAME')
    # name = fields.Char(string="NAME", compute="_get_full_name" )
    id_card = fields.Integer(string="ID CARD")
    ward_num = fields.Char(string="ROOM NUMBER")
    # code = fields.Char(string='CODE')
    age = fields.Integer(string= "AGE")
    doctor_address = fields.Text(string="Doctor Address")
    doctor_photo = fields.Binary(string="Doctor Photo", attachment=True)
    date_of_birth = fields.Date(
                string='Date of birth', default=datetime.today())
    today_deauty_id= fields.One2many('nurse.addon', 'deauty_under_ids', string = "Nurse With")
    # diseases_specialist = fields.Char (string="specialist")
    # diseases_depts = fields.Many2many('patient.addon' , string = "Diseases specialist Doc")