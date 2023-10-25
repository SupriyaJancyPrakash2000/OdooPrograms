from odoo import api, fields, models, _

class SaleOrder(models.Model):
    _inherit = "crm.lead"