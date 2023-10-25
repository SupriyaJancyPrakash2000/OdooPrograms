from dateutil.relativedelta import relativedelta
from datetime import date, timedelta, datetime
from odoo import models, fields, api

from odoo.tools.date_utils import start_of, end_of


class SickCasualCheck(models.Model):
    _inherit = 'hr.leave'

    def scheduleaccrual(self):

        casual_leave_type_id = self.env['hr.leave.type'].search([('id', '=', 1)])
        sick_leave_type_id = self.env['hr.leave.type'].search([('id', '=', 2)])

        current_date = fields.Date.today()
        first_day = start_of(current_date, "month")
        print(".......................",first_day)
        last_day = end_of(current_date, "month")
        print(".......................", last_day)

        last_day_of_prev_month = date.today().replace(day=1) - timedelta(days=1)
        start_day_of_prev_month = date.today().replace(day=1) - timedelta(days=last_day_of_prev_month.day)
        print(start_day_of_prev_month)
        print(last_day_of_prev_month)



        employee = self.env['hr.employee'].search([('contract_ids.state', '=', 'open'), ('active', '=', True)])
        print(employee)

        for emp in employee:
            print(emp)

            duration = 0
            number_of_day = 3

            #check whether the employee has casual leave allocation in previous month or not
            previous_casual_leave_alloc = self.env['hr.leave.allocation'].search([
                ('employee_id', '=', emp.id),
                ('holiday_status_id', '=', casual_leave_type_id.id),
                ('date_from', '=', start_day_of_prev_month),
                ('date_to', '=', last_day_of_prev_month),
            ])
            if previous_casual_leave_alloc:
                number_of_casual_leave = previous_casual_leave_alloc.number_of_days
                print("------------------", number_of_casual_leave)

                #check whether the employee had casual leave in previous month
                casual_leave = self.env['hr.leave'].search([
                    ('employee_id', '=', emp.id),
                    ('holiday_status_id', '=', casual_leave_type_id.id),
                    ('date_from', '<=', last_day_of_prev_month),
                    ('date_to', '>=', start_day_of_prev_month),
                ])

                if casual_leave:
                    print("&&&&&&&&&&&&&&&&&")
                    duration = number_of_casual_leave
                    for each_rec in casual_leave:
                        duration = duration-each_rec.number_of_days_display
                        print("%%%%%%%%%%%%%%%%%%%%%%%%%", duration)

                else:
                    duration = number_of_casual_leave



            #Casual leave allocation for each active employee
            casual_leave_alloc = self.env['hr.leave.allocation'].search([
                ('employee_id', '=', emp.id),
                ('holiday_status_id', '=', casual_leave_type_id.id),
                ('date_from', '=', first_day),
                ('date_to', '=', last_day),
            ])
            days = number_of_day + duration
            print(":::;;;;;;;+++++++++++++++", days)
            if not casual_leave_alloc:
                self.env['hr.leave.allocation'].create({
                    'name': 'Casual Time off',
                    'employee_id': emp.id,
                    'date_from': first_day,
                    'date_to': last_day,
                    # 'state': 'validate',
                    'number_of_days': days,
                    'holiday_status_id': casual_leave_type_id.id

                }).action_confirm()
                print("Casual###########################")



                # Sick leave allocation for each active employee
                sick_leave_alloc = self.env['hr.leave.allocation'].search([
                    ('employee_id', '=', emp.id),
                    ('holiday_status_id', '=', sick_leave_type_id.id),
                    ('date_from', '=', first_day),
                    ('date_to', '=', last_day),
                ])

                if not sick_leave_alloc:
                    self.env['hr.leave.allocation'].create({
                        'name': 'Sick Time off',
                        'employee_id': emp.id,
                        'date_from': first_day,
                        'date_to': last_day,
                        # 'state': 'validate',
                        'number_of_days': 3,
                        'holiday_status_id': sick_leave_type_id.id

                    }).action_confirm()
                    print("sick$$$$$$$$$$$$$$$$$$$$$$$$$$$$")




