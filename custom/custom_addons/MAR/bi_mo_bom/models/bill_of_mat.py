from odoo import fields,api,models,exceptions

class BillOfMat(models.Model):
    _inherit = 'mrp.bom'

    bill_mat_line_ids = fields.One2many('product.variant.lines', 'bill_of_mat_id')
    mo_count = fields.Integer(compute='compute_count')


    @api.onchange('product_tmpl_id')
    def create_product_variant_line(self):
        variant_lines = []
        product_variants = self.env['product.product'].search([('product_tmpl_id', '=', self.product_tmpl_id.id)])
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", product_variants)
        for rec in product_variants:
            new_line = self.env['product.variant.lines'].create({
                'product_variants': rec.id,
                'quant': 1

            })
            variant_lines.append(new_line.id)
        self.bill_mat_line_ids = [(6, 0, variant_lines)]

    def create_mo(self):

        for each in self.bill_mat_line_ids:
            product_comp_list = []
            for each_comp in self.bom_line_ids:
                uom_qty = (each.ratio / 100) * each_comp.product_qty
                product_comp_list.append((0, 0, {
                    'product_id': each_comp.product_id.id,
                    'product_uom_qty': uom_qty,
                    'product_uom': each_comp.product_uom_id.id
                }))
            self.env['mrp.production'].create({
                'product_id': each.product_variants.id,
                'move_raw_ids': product_comp_list,
                'product_qty': uom_qty,
                'bom_id': self.id
            }).action_confirm()



    def compute_count(self):
        for record in self:
            record.mo_count = self.env['mrp.production'].search_count(
                [('bom_id', '=', self.id)])
            print("****************")


    def mo_view(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'MO',
            'view_mode': 'tree,form',
            'res_model': 'mrp.production',
            'domain': [('bom_id', '=', self.id)],

        }
    print("&&&&&&&&&&&&&&&&&&")



class BillOfMatLine(models.Model):
    _name = 'product.variant.lines'

    bill_of_mat_id = fields.Many2one("mrp.bom")
    product_variants = fields.Many2one('product.product', string="Product Variant")
    quant = fields.Integer(string="Quantity")
    ratio = fields.Float(string="Ratio")
    # uom_id = fields.Many2one('uom.uom', string="UoM")
    uomid = fields.Many2one('uom.uom', string="UoM")