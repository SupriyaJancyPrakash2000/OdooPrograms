from odoo import models,fields,api,_

class SalesOrder(models.Model):
    _inherit= 'account.move'

    invoice_id = fields.Many2one('sales.shop',string="Invoice")
