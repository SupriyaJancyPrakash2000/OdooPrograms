from odoo import fields,models

class Invoiceheck(models.Model):
    _inherit = "purchase.order.line"

    select = fields.Boolean(string="Select")

    def _prepare_account_move_line(self):
        if self.select:
          purchase_order_line = super(Invoiceheck, self)._prepare_account_move_line()
          purchase_order_line['select'] = True
          return purchase_order_line
        else:
          return super(Invoiceheck, self)._prepare_account_move_line()