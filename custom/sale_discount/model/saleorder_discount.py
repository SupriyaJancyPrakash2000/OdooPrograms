# from odoo import api, fields, models

# class SaleOrderDiscountField(models.Model):
#     _inherit = 'sale.order'
    
    
  
    
#     def add_discount(self):
#         for order in self:

#             if order.dicount:
#                 product = self.env['product.product'].search([('check_discount', '=', True)])
                
#                 discount_amount = product.lst_price * (order.dicount / 100)

               
#                 existing_discount_line = order.order_line.filtered(lambda line: line.product_id == product and line.price_unit < 0)
                
#                 if existing_discount_line:
                  
#                     existing_discount_line.price_unit = -(order.amount_total * order.dicount / 100)
#                 else:
                  
#                     discount_line = self.env['sale.order.line'].create({
#                         'product_id': product.id,
#                         'product_uom_qty': 1,
#                         'price_unit': -(order.amount_total * order.dicount / 100), 
#                         'dicount': 0.0,
#                         'tax_id': False,
#                         'order_id': order.id
#                     })

# class ProductDiscountField(models.Model):
#     _inherit = 'product.product'
    
#     check_discount = fields.Boolean(string='Discount true', default=False)