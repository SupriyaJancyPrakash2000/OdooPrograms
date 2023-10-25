from odoo import fields,models

class SalaryHike(models.Model):
    _inherit = 'hr.contract'

    arrears_boolean = fields.Boolean(string="Hike Bool")

