from odoo import fields,models
 
class MateialTransfer(models.Model):
    _name = 'material.transfer'
    _rec_name= 'id'

    from_loc = fields.Many2one('stock.location',string="From Location")
    to_loc = fields.Many2one('stock.location',string="To Location",domain="[('usage', '=', 'internal')]")
    transfer_line_connection = fields.One2many('material.transferline','material_line_id')
    partner_id = fields.Many2one('res.partner',string="Partner") 
    service_pick_id = fields.One2many('stock.picking','product_pick_con_ids')
    trans_count = fields.Integer(compute="compute_trans_count",string="Transfer count")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('transfer', 'Transfer'),
        ('receive', 'Receive'),
        ('return', 'Return')
     ],default='draft')


    def compute_trans_count(self):
        pick_search = self.env['stock.picking'].search_count([('product_pick_con_ids','=',self.id)])
        self.trans_count = pick_search
    

    
    def product_transfer(self):
        pick_type=self.env['stock.picking.type'].search([('sequence_code','=','INT')],limit=1)
        lines_vals = []

        for line in self.transfer_line_connection:
            lines_vals.append((0, 0, {
                'name': line.product_id.display_name,
                'product_id': line.product_id.id,
                'product_uom_qty': line.quantity,
                'product_uom': line.product_id.uom_id.id,
                'location_id': self.from_loc.id,
                'location_dest_id': self.to_loc.id,
                'quantity_done' : line.quantity,
            }))
        vals = {
            'partner_id': self.partner_id.id,
            'location_id': self.from_loc.id,
            'location_dest_id': self.to_loc.id,
            'picking_type_id': pick_type.id,
            'state': 'draft',
            'move_ids_without_package': lines_vals,
            'product_pick_con_ids':[(4, self.id)]
        }
        picking = self.env['stock.picking'].create(vals)
        picking.action_confirm()
        picking.action_assign()
        # picking.button_validate()

        self.write({'state': 'transfer'})

    def product_receive(self):
        picking = self.env['stock.picking'].search([('product_pick_con_ids', '=', self.id)])
        picking.button_validate()
        self.write({'state': 'receive'})

    def product_return(self):
        pick_type=self.env['stock.picking.type'].search([('sequence_code','=','INT')],limit=1)
        lines_vals = []
        for line in self.transfer_line_connection:
            lines_vals.append((0, 0, {
                'name': line.product_id.display_name,
                'product_id': line.product_id.id,
                'product_uom_qty': line.quantity,
                'product_uom': line.product_id.uom_id.id,
                'location_id': self.to_loc.id,
                'location_dest_id': self.from_loc.id,
                'quantity_done' : line.quantity,
            }))
        vals = {
            'partner_id': self.partner_id.id,
            'location_id': self.to_loc.id,
            'location_dest_id': self.from_loc.id,
            'picking_type_id': pick_type.id,
            'state': 'draft',
            'move_ids_without_package': lines_vals,
            'product_pick_con_ids':[(4, self.id)]
        }
        picking = self.env['stock.picking'].create(vals)
        picking.action_confirm()
        picking.action_assign()
        picking.button_validate()

        self.write({'state': 'return'})


    def material_picking(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Product picking',
            'view_mode': 'tree,form',
            'res_model':'stock.picking',
            'domain': [('product_pick_con_ids', '=', self.id)]
        }

    

class MaterialTransferLine(models.Model):
    _name = 'material.transferline'

    material_line_id = fields.Many2one('material.transfer')
    product_id = fields.Many2one('product.product',string="Product")
    quantity = fields.Integer(string="Quantity")



class MaterialTransferPick(models.Model):
    _inherit = 'stock.picking'

    product_pick_con_ids = fields.Many2many('material.transfer')


