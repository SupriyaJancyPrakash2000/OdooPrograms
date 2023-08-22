from odoo import fields,models,_

class ReasonNote(models.Model):
    _inherit = 'purchase.order'

    review = fields.Text(string="Reason")
    count = fields.Integer(string="Number of lines")

    def reason(self):
        return {
            'name': _("create wizard"),
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'wizard.view.reason',
            'target': 'new',
            'context':{
                'default_purchase_id':self.id
            }
        }