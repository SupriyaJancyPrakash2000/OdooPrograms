from odoo import fields,models,api

class ScheduleSale(models.Model):
   _inherit= 'sale.order'

   sale_order_check = fields.Boolean(string="Sale order check")


   def update_sale_order(self):
         records = self.env['sale.order'].search([])
         for rec in records:
             if rec.state == 'draft':
                rec.sale_order_check = True
             else:
                 rec.sale_order_check = False
        