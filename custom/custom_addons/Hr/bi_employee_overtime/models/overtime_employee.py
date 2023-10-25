from dateutil.relativedelta import relativedelta
from odoo import fields, api,models

class LoanAllocation(models.Model):
    _name = 'employee.payroll'

    emp_id = fields.Many2one('hr.employee',string="Employee")
    hours_worked = fields.Integer(string="Hourse Worked")
    no_of_days = fields.Integer(string="Number of Days")
    loan_lines = fields.One2many('employee.payrolllines','lines_id')
    date = fields.Date(string="Date")
    state = fields.Selection([
        ('draft','Draft'),
        ('approve','Approved')
    ],
    default='draft')
   

    def overtime_action(self):
        new_lines = []
        current_date = self.date
        hours = self.hours_worked
        for each in range(self.no_of_days):
                new_line = self.env['employee.payrolllines'].create({
                    'date':current_date,
                    'hours_worked':hours
                })
                current_date = current_date+relativedelta(days=1)
                new_lines.append(new_line.id)
        self.loan_lines = [(6, 0, new_lines)]


class LoanAllocationLine(models.Model):
    _name="employee.payrolllines"

    lines_id = fields.Many2one('employee.payroll')
    date = fields.Date(string="Date")
    hours_worked = fields.Integer(string="Hours Worked")