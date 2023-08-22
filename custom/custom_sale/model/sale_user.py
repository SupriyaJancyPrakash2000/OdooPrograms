from odoo import api, fields, models

class SaleUser(models.Model):
    _inherit = "sale.order"

    set_user_field = fields.Many2one('res.users',string="Set User",default=lambda self: self.env.user if self.env.user.has_group('custom_sale.overtime_managers_access') else False)
    check_sale_order_confirm = fields.Boolean(string="Check Confirm")

    def action_confirm(self):
        # Call the parent method to execute the original behavior of action_confirm
        res = super(SaleUser, self).action_confirm()

        # Set the is_confirmed field to True
        self.write({'check_sale_order_confirm': True})
        return res
    
    def _prepare_invoice(self):
        invoice_vals = super(SaleUser, self)._prepare_invoice()
        invoice_vals['is_invoice_create'] = True
        return invoice_vals




#default=lambda self: self.env.user

    # @api.model
    # def create(self, vals):
    #     vals['set_user_field'] = self.env.user.id
    #     res = super(SaleUser, self).create(vals)
    #     return res

    # @api.model
    # def create(self, vals):
    #     res = super(SaleUser, self).create(vals)
    #     current_user = self.env.user
    #     if current_user.has_group('custom_sale.overtime_managers_access'):
    #         vals['set_user_field'] = current_user.id
    #         res_new = super(SaleUser, self).create(vals)
    #         return res_new
    #     else:
    #         return res
