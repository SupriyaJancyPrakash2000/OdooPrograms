from odoo import models,fields,api,_

class SalesProduct(models.Model):
    _inherit= 'product.template'

    checklist = fields.Boolean(string="Check List")
    product_check = fields.Boolean(string="Product Check",default=False)