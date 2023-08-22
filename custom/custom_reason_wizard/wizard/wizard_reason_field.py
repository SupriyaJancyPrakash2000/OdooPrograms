from odoo import fields,models,api,_

class ReviewWizard(models.TransientModel):
    _name= "wizard.view.reason"
    

    reason = fields.Text(string='Description')
    purchase_id = fields.Many2one('purchase.order',string="Purchase")
    sale_id = fields.Many2one('sale.order', string="Sale Order")
    
    def pass_review(self):
        rec = self.env['sale.order'].search([('id', '=', self.sale_id.id)])
        num = len(rec.order_line)
        self.purchase_id.write({'count': num})
        self.purchase_id.write({'review': self.reason})
        
