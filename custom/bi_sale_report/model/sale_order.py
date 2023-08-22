from odoo import api, fields, models, _

class SaleOrder(models.Model):
    _inherit = "sale.order"

    vend_id = fields.Many2one('account.move',string="Vendor")

    

    # def print_sale_report(self):
    #     action = self.env.ref("bi_sale_report.action_custom_sale_report").report_action(self.id)
    #     return action