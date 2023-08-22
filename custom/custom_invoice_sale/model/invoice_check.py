from odoo import fields,models

class Invoiceheck(models.Model):
    _inherit = "account.move.line"

    select = fields.Boolean(string="Select")