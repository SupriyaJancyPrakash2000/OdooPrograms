from odoo import api, fields, models

class ChangeInvoice(models.Model):
    _inherit = "account.move"

    is_invoice_create = fields.Boolean(string="Check")