from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit = "sale.order"

    short_note = fields.Char(string="Short Notes")
    vend_id = fields.Many2one('account.move',string="Vendor")


class SalesOrderLine(models.Model):
    _inherit = "sale.order.line"

    purchase_id = fields.Many2one('purchase.order',string="Purchase")

