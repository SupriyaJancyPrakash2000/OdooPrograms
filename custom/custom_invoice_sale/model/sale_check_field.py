from odoo import fields,models

class SaleCheck(models.Model):
    _inherit = "sale.order.line"

    select = fields.Boolean(string="Select")