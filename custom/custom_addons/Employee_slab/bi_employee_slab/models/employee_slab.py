from odoo import models,fields, api

class EmployeeSlab(models.Model):
    _name = "employee.slab"

    employee_id = fields.Many2one('hr.employee',string="Employee")
    tds_salary = fields.Float(string="Tds salary")
    tds_month = fields.Float(string="Tds monthly")
    gross_salary = fields.Float(string="income(anum)")
    income_month = fields.Float(string="income(month")
    expence = fields.Float(string="Expence")
    expence_monthly = fields.Float(string="Yearly Expence")
    yearly_salary = fields.Float(string="yearly salary")
    tax = fields.Float(string="Tax percentage")
    year_wise = fields.Many2one('employee.year', string= "Year wise")
    employee_line_ids = fields.One2many('employee.slab.lines', 'employee_line_id')
    @api.onchange('employee_id')
    def employee_slab(self):
        employee = self.env['hr.contract'].search([('employee_id', '=', self.employee_id.id)])
        if employee:
            emp_wage = employee.wage
            self.gross_salary = emp_wage * 12
            self.income_month = self.gross_salary/12
            emp_expence = 150000
            self.expence = emp_expence
            self.expence_monthly = self.expence
            self.yearly_salary = self.gross_salary - self.expence_monthly

    @api.onchange('tax')
    def tds_slab(self):
        self.tds_month = ((self.yearly_salary * self.tax)/100)/12
        self.tds_salary = (self.yearly_salary * self.tax)/100
        tds = self.env['hr.contract'].search([('employee_id','=',self.employee_id.id)])
        tds.update({"tds_slab":self.tds_month})

    @api.onchange('year_wise')
    def slab_year(self):
       year = self.yearly_salary
       tax = 0
       for line in self.year_wise.year_connection_ids:
           print(">>>>>>>>>>>>>>>>>>>>>>>>>forrr   line",line)
           if year >= line.income and year<=line.upto:
               print(">>>>>>>>>>>>>>>>>iffffff")
               tax = line.tax_slab
               break

       self.tax = tax