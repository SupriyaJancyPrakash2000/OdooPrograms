from dateutil.relativedelta import relativedelta
from datetime import date, timedelta, datetime
from odoo import models, fields, api

class AttendanceCheck(models.Model):
    _inherit = 'hr.leave'

    def scheduleemployeelop(self):


        leave_type_id = self .env['hr.leave.type'].search([('id', '=', 6)])
        print(leave_type_id)
        last_day_of_prev_month = date.today().replace(day=1) - timedelta(days=1)
        start_day_of_prev_month = date.today().replace(day=1) - timedelta(days=last_day_of_prev_month.day)
        print(start_day_of_prev_month)
        print(last_day_of_prev_month)
    

        employee = self.env['hr.employee'].search([('contract_ids.state', '=', 'open'),('active', '=', True)])
        print(employee)

        for emp in employee:
            print(emp)
            att = self.env['hr.attendance'].search([
                ('employee_id', '=', emp.id),
                ('check_in', '>=', start_day_of_prev_month),
                ('check_in', '<=', last_day_of_prev_month),
            ])
            check_in = att.mapped("check_in")
            list_check_in = []
            for each in check_in:
                list_check_in.append(each.date())
            start_date = start_day_of_prev_month
            while start_date<=last_day_of_prev_month:
                if start_date not in list_check_in:
                    leave_rec = self.env['hr.leave'].search([('employee_id', '=', emp.id),
                                                        ('state', '=', 'validate'),
                                                        ('request_date_from', '<=', start_date),
                                                        ('request_date_to', '>=', start_date)])
                    if start_date.strftime("%A") == "Saturday" or start_date.strftime("%A") == "Sunday":
                        pass
                    else:
                            if not leave_rec:
                                leave = self.env['hr.leave'].create({
                                    'name': 'leave',
                                    'holiday_type': 'employee',
                                    'employee_id': emp.id,
                                    'holiday_status_id': leave_type_id.id,
                                    'date_from': start_date,
                                    'date_to': start_date,
                                    'number_of_days': 1.0,
                                    'notes': 'Additional notes here',
                                    'request_date_from': start_date,
                                    'request_date_to': start_date,
                                })
                                leave.action_approve()
                                leave.action_validate()



                                print('rrrrr')

                start_date += relativedelta(days=1)
                  

               