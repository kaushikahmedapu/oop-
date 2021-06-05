from odoo import models,fields,api, _
from datetime import datetime
from odoo.exceptions import UserError



class Patient(models.Model):
    _name = "patient.addon"
    _description = "test"
    


    bill = fields.Integer(string='BILL')
    discount = fields.Integer(string='DISCOUNT')
    total = fields.Integer(string='TOTAL BILL',compute='_get_total')
    name = fields.Char(string="NAME")
    serial_number = fields.Integer(string="Serial Number")
    # ward_num = fields.Char(string="ROOM NUMBER")
    # code = fields.Char(string='CODE')
    age = fields.Integer(string= "AGE")
    patient_address = fields.Text(string="patient Address")
    patient_photo = fields.Binary(string="patient Photo", attachment=True)
    date_of_birth = fields.Date(
                string='Date of birth', default=datetime.today())
    
    disease_dept = fields.Selection([('neurologist',"Neurologist"),
                               ('psychiatrist',"Psychiatrist"),
                               ('radiologist',"Radiologist")],
                                string="Disease Dept")

    disease_depts_ids = fields.Many2many('doctor.addon', string= "Doctor assign")
    code = fields.Char(string='CODE')
    # # @api.depends('fname')
    # def get_total(self):
        
    #     for item in self:
    #         bill= 0
    #         discount= 0
    #         if item.fname > 0:
    #             bill = self.fname
    #         if item.lname >0:
    #             discount = self.lname
    #         return bill - discount
                
              


    def _get_total(self):
        for item in self:

            bill = 0
            discount = 0
            if item.bill > 0:
                bill = item.bill
            if item.discount > 0:
                discount = item.discount

            item.total = bill - discount
        
    # def _get_total(self):
    #     for item in self:
    #         item.total = item.final_price()



    @api.onchange('code')
    def onchange_code(self):
        exist = self.env['patient.addon'].search([])
        if self.code:
            for i in exist:
                if self.code == i.code:
                    raise UserError(_("This Code Already exist"))

    def write(self, values):
        code_exist = self.env ['patient.addon'].search([('code', '=', values['code'])])
        if code_exist:
            raise UserError(_("This Code Already exist"))
        result = super(Patient, self).write(values)
        return result 

     
    @api.model
    def create(self, values):
        code_exist = self.env ['patient.addon'].search([('code', '=', values['code'])])
        if code_exist:
            raise UserError(_("This Code Already exist"))
        result = super(Patient, self).create(values)
        return result    