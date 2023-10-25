from odoo import models,fields,api

class EmployeeSlabLines(models.Model):
    _name = "employee.slab.lines"

    income = fields.Char(strind="income")
    upto = fields.Char(string="upto")
    tax_slab = fields.Char(string="Tax slab")
    employee_line_id = fields.Many2one('employee.slab', string="Year connection")