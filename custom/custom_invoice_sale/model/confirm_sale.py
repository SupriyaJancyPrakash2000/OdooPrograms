from odoo import api, fields, models

class SaleInvoice(models.Model):
    _inherit = "sale.order"

    check_sale_order_confirm = fields.Boolean(string="Check Confirm")

    def action_confirm(self):
        # Call the parent method to execute the original behavior of action_confirm
        res = super(SaleInvoice, self).action_confirm()

        # Set the is_confirmed field to True
        self.write({'check_sale_order_confirm': True})
        return res
    
    def _prepare_invoice(self):
        invoice_vals = super(SaleInvoice, self)._prepare_invoice()
        invoice_vals['is_invoice_create'] = True
        return invoice_vals
    
    def _create_invoices(self, grouped=False, final=False, date=None):
        moves = super()._create_invoices(grouped=grouped, final=final, date=date)
        for invoice_line in moves['invoice_line_ids']:
            for line in self.order_line:
                if line.product_id.id == invoice_line.product_id.id:
                    if line.select == True:
                        invoice_line.select = True
        return moves
    