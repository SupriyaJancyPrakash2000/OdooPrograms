# from odoo import api, fields, models


# class ShopOrderEntry(models.Model):
#     _name= "custom.sales.order"
#     _rec_name= "shop_name"

#     shop_name = fields.Char(string="Shop Name")
#     place = fields.Char(string="Place") 
#     amount = fields.Float(string="Amount")
#     count = fields.Integer(string="Count",default=6)
#     sales_shop_line = fields.One2many('custom.sales.shop.line','sales_shop_line_id')

# class ShopOrderLine(models.Model):
#     _name= "custom.sales.shop.line"

#     sales_shop_line_id = fields.Many2one("custom.sales.order")
#     month = fields.Char(string="Month")
#     amount = fields.Float(string="Amount")