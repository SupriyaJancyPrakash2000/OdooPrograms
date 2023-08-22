from odoo import fields,models

class AutoWorkFlow(models.Model):
    _inherit = 'sale.order'

    auto_work_flow = fields.Boolean(string="Auto Workflow")

    def action_confirm(self):
        # Call the parent method to execute the original behavior of action_confirm
        res = super(AutoWorkFlow, self).action_confirm()
        if self.auto_work_flow == True:
            self._create_invoices()
            for each in self.invoice_ids:
                each.action_post()
            delivery = self.env['stock.picking'].search([('sale_id', '=', self.id)])
            delivery.action_set_quantities_to_reservation()
            delivery.button_validate()
        return res
        
