from odoo import models, fields

class EmployeeYear(models.Model):
    _name = "employee.year"
    _rec_name = "years"

    years = fields.Char(string="Year")
    year_connection_ids = fields.One2many('employee.year.lines','year_connect_id')




class EmployeeYearLine(models.Model):
    _name = "employee.year.lines"

    income = fields.Integer(strind="income")
    upto = fields.Integer(string="upto")
    tax_slab = fields.Integer(string="Tax slab(%)")
    year_connect_id = fields.Many2one('employee.year',string="Year connection")