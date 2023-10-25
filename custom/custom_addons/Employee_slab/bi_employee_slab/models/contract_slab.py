from odoo import fields,models

class HrContract(models.Model):
    _inherit = "hr.contract"

    tds_slab = fields.Float(string="TDS")