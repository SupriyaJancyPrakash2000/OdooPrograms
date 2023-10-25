from odoo import models, api, exceptions
from datetime import date, timedelta
from datetime import datetime
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError

class CheckPublicHoliday(models.Model):
    _inherit = 'hr.leave'

#1st method using constarins
    @api.constrains('request_date_from','request_date_to')
    def _check_date_end(self):
        start_date = self.request_date_from
        end_date = self.request_date_to
        records = self.env['resource.calendar.leaves'].search([('date_from','<=',end_date ),('date_to','>=', start_date)])
        if records:
            raise exceptions.UserError("It Is already a Public holiday")
        
        first_date = start_date
        while(first_date<=end_date):
            if first_date.strftime("%A") in ['Saturday', 'Sunday']:  
                raise exceptions.UserError("It Is a weekend....")
            first_date += timedelta(days=1) 
            
#2nd method using create and write

    # @api.model
    # def create(self, vals):  

    #     res = super(CheckPublicHoliday, self).create(vals)

    #     request_date_from = vals.get('request_date_from')
    #     request_date_to = vals.get('request_date_to')
    #     date_from_object = datetime.strptime(request_date_from, '%Y-%m-%d').date()
    #     date_to_object = datetime.strptime(request_date_to, '%Y-%m-%d').date()
       
    #     public_holiday_type =self.env['resource.calendar.leaves'].search([('date_from','>=',date_to_object ),('date_to','<=', date_from_object)])
        
    #     if public_holiday_type:
    #         raise exceptions.UserError("It Is already a Public holiday")
        
    #     if date_from_object.strftime("%A") in ['Saturday', 'Sunday']:  
    #         raise exceptions.UserError("It Is A Public holiday (Saturday or Sunday)")
        
    #     return res
        
        
    
    # def write(self,vals):

    #     res = super(CheckPublicHoliday, self).write(vals)

    #     start_date = self.request_date_from
    #     end_date = self.request_date_to
    #     records = self.env['resource.calendar.leaves'].search([('date_from','<=',end_date ),('date_to','>=', start_date)])
    #     if records:
    #         raise exceptions.UserError("It Is already a Public holiday")
        
    #     first_date = start_date
    #     while(first_date<=end_date):
    #         if first_date.strftime("%A") in ['Saturday', 'Sunday']:  
    #             raise exceptions.UserError("It Is A Public holiday (Saturday or Sunday)")
    #         first_date += timedelta(days=1) 
            
    #     return res
    

    
        




   


    

