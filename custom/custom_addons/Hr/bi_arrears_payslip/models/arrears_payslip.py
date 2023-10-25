from odoo import fields,models

class ArrearsSetUp(models.Model):
    _name = 'salary.arrears'

    employee_id = fields.Many2one('hr.employee', string="Employee")
    arrear_amount = fields.Integer(string="Hike")
    effective_from_month = fields.Date(string="Month")
    arrears_boolean = fields.Boolean(string="Hike Bool")
    salary = fields.Integer(string="Salary")

    def allocate_arrears(self):
        employee = self.env['hr.contract'].search([('employee_id', '=', self.employee_id.id)])
        self.salary = employee.wage+self.arrear_amount


        # if employee:
        #     employee.arrears = self.arrear_amount