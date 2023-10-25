from dateutil.relativedelta import relativedelta
from odoo import fields, api,models

class LoanAllocation(models.Model):
    _name = 'loan.payroll'

    emp_id = fields.Many2one('hr.employee',string="Employee")
    date = fields.Date(string="Date")
    amount = fields.Integer(string="Amount")
    no_of_instal = fields.Integer(string="Number of Installment")
    loan_lines = fields.One2many('loan.payrolllines','lines_id')
    state = fields.Selection([
        ('draft','Draft'),
        ('approve','Approved')
    ],
    default='draft')
    check = fields.Boolean(string="Check")

    def loan_action(self):
        newloan_lines = []
        current_date = self.date
        split_amt = self.amount/self.no_of_instal
        for each in range(self.no_of_instal):
                new_line = self.env['loan.payrolllines'].create({
                    'date':current_date,
                    'amount':split_amt
                })
                current_date = current_date+relativedelta(months=1)
                newloan_lines.append(new_line.id)
        self.loan_lines = [(6, 0, newloan_lines)]


class LoanAllocationLine(models.Model):
    _name="loan.payrolllines"

    lines_id = fields.Many2one('loan.payroll')
    amount = fields.Integer(string="Amount")
    date = fields.Date(string="Date")