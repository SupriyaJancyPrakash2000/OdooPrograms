from odoo import fields,models

class EmployeeLoan(models.Model):
    _name = 'employee.loan'

    emp_id = fields.Many2one('hr.employee',string="Employee")
    amt = fields.Integer(string="Amount")
    state = fields.Selection([
        ('draft','Draft'),
        ('post','posted')
    ])
    
   

    def Loan_action(self):
        self.write({'state':'post'})
    

