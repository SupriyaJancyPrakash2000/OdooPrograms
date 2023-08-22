from odoo import fields,models  

class SaleToPurchase(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        res=super(SaleToPurchase, self).action_confirm()

        lines_vals = []
        for line in self.order_line:
            lines_vals.append((0, 0, {
                'name': line.product_id.name,
                'product_id': line.product_id.id,
                'product_qty': line.product_uom_qty,
            }))
        vals = {
            'partner_id': self.partner_id.id,
            'order_line':lines_vals,
            'sale_id':self.id,
        }
        purchase = self.env['purchase.order'].create(vals)
        purchase.button_confirm()
        for rec in purchase.picking_ids:
            for line in rec.move_ids_without_package:
                line.quantity_done = line.product_uom_qty
        rec.button_validate()

        for rec in self.picking_ids:
            for line in rec.move_ids_without_package:
                line.quantity_done = line.product_uom_qty
        rec.button_validate()

        return res
    

class SaleInPurchase(models.Model):
    _inherit = 'purchase.order'

    sale_id = fields.Many2one('sale.order')