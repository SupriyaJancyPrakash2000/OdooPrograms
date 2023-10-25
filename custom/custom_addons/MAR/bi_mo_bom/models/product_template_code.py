from odoo import models,fields,api,_

class ProductCode(models.Model):
    _inherit = 'product.template'

    code_pro = fields.Char(string="Code")
