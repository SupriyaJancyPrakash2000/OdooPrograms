from odoo import models, api, exceptions,fields
from datetime import date, timedelta
from datetime import datetime
from dateutil.relativedelta import relativedelta

class CheckPublicHoliday(models.Model):
    _inherit = 'hr.leave'

    joining_date = fields.Date(string="Joining Date")

    @api.onchange('request_date_from','request_date_to')
    def check_joining(self):

        start_date = self.request_date_from
        end_date = self.request_date_to
        
        list_date = []

            
        if end_date.strftime("%A") in ['Friday']:
            end_date += timedelta(days=3)

        else:
            if end_date.strftime("%A") in ['Saturday', 'Sunday']:
                end_date += timedelta(days=1)
        
        records = self.env['resource.calendar.leaves'].search([('date_from','<=',end_date ),('date_to','>=', start_date)])
        if records:
            first = records.date_from
            end = records.date_to
            date_from = first.date()
            date_to = end.date()
            while(date_from<=date_to):
                list_date.append(date_from)
                date_from += relativedelta(days = 1)
            if end_date in list_date:
                end = list_date[-1]
                end += timedelta(days=1)
                end_date = end

            else:
                end_date += timedelta(days=1)
        
        self.joining_date = end_date
    
      



  