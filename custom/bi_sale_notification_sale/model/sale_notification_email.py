from odoo import fields,models,_

class NotificationEmailInSale(models.Model):
    _inherit = 'sale.order'

    def approve(self):
         return {
            'name': _("create wizard"),
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'sale.approve.wizard',
            'target': 'new',
            'context':{
                'default_sale_id':self.id
            }
        }


