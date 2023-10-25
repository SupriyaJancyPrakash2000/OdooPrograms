from odoo import fields,models

class FieldEmployee(models.Model):
    _inherit = "hr.employee"

    pan = fields.Char(string="PAN Number")
    esi = fields.Char(string="ESI Number")
    uan = fields.Char(string="UAN Number")
