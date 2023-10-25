from odoo import fields,api,models,exceptions,_

class ExcelImport(models.Model):
    _inherit = 'mrp.bom'


    def bring_components(self):
        print("&&&&&&&&&&&&&&&&&&")
        return {
            'name': _("create wizard"),
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'excel.wizard',
            'target': 'new',
            'context': {
                'default_mrp_id': self.id
            }
        }





