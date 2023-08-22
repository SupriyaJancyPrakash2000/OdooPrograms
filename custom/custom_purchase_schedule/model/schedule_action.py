from odoo import fields,models

class PurchaseSchedule(models.Model):
    _inherit = 'purchase.order'
    
    
    def update_purchase_order(self):
        records = self.env['purchase.order'].search([])
        for rec in records:
            if rec.state == 'draft':
                rec.button_cancel()