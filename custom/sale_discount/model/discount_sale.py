from odoo import fields,models,api


class DiscountSale(models.Model):
    _inherit = 'sale.order'

    dicount = fields.Integer(string="Discount")

    @api.onchange('dicount')
    def dis_amount(self):
        for line in self.order_line:
            line.dicount_line = self.dicount

     
    def add_discount(self):
        for each in self:

            if each.dicount:
                product = self.env['product.product'].search([('check_discount', '=', True)])
                if product:
                    for line in each.order_line:
                        if line.product_id == product:
                            line.unlink()
                    self.env['sale.order.line'].create({
                                'product_id': product.id,
                                'product_uom_qty': 1,
                                'price_unit': -(each.amount_total * each.dicount / 100), 
                                'discount':0.0,
                                'order_id':each.id,
                                'tax_id': False,
                                'name':'Discount',
                            
                            })



class ProductDiscountField(models.Model):
    _inherit = 'product.product'
    
    check_discount = fields.Boolean(string='Discount true', default=False)
    

class DiscountSale(models.Model):
    _inherit = 'sale.order.line'

    dicount_line = fields.Integer(string="Discount")

        
