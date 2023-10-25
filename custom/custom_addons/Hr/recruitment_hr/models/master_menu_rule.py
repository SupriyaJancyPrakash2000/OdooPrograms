from odoo import fields,models

class SalaryEmpRule(models.Model):
    _name = 'emp.salary.rules'

    name = fields.Char(string="Name")
    perc = fields.Float(string="Percentage")
    categ_id = fields.Many2one('hr.salary.rule.category', string="Category")

