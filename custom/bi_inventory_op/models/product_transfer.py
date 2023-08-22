from odoo import fields,models

class ProductMov(models.Model):
    _name = 'product.move_service'

    from_loc = fields.Many2one('stock.location',string="From Location")
    to_loc = fields.Many2one('stock.location',string="To Location",domain="[('usage', '=', 'internal')]")
    # partner = fields.Many2one('res.partner',string="Partner")
    stock_line_ids = fields.One2many('product.stockline','product_move_line_id')
    # pick_id = fields.Many2one('stock.picking')
    service_pick_id = fields.One2many('stock.picking','product_pick_con_ids')
    trans_count = fields.Integer(compute="compute_trans_count",string="Invoice count")

    def compute_trans_count(self):
        pick_search = self.env['stock.picking'].search_count([('product_pick_con_ids','=',self.id)])
        self.trans_count = pick_search


    state = fields.Selection([
        ('draft', 'Draft'),
        ('move', 'Move'),
        ('return', 'Return')
     ], default='draft')
    # link_field_id = fields.One2many('inventory.move', 'connection_id', string="Link Field")
    partner_id = fields.Many2one("res.partner", string="Partner")
    
    
    def product_move(self):
        pick_type=self.env['stock.picking.type'].search([('sequence_code','=','INT')],limit=1)
        lines_vals = []

        for line in self.stock_line_ids:
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
        picking.button_validate()

        self.write({'state': 'move'})
  
    def product_return(self):
        pick_type=self.env['stock.picking.type'].search([('sequence_code','=','INT')],limit=1)
        lines_vals = []
        for line in self.stock_line_ids:
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

    def product_picking(self):
        self.ensure_one()
        return {
                'type': 'ir.actions.act_window',
                'name': 'Picking view',
                'view_mode': 'tree,form',
                'res_model': 'stock.picking',
                'domain': [('product_pick_con_ids', '=', self.id )],
            }




class ProductMovLine(models.Model):
    _name = 'product.stockline'

    product_move_line_id = fields.Many2one('product.move_service') 
    product_id = fields.Many2one('product.product',string="Product")
    quantity = fields.Integer(string="Quantity")


class StockLocation(models.Model):
    _inherit = 'stock.location'

    check_internal = fields.Boolean(string="Check Internal")

class StockTransPick(models.Model):
    _inherit = 'stock.picking'

    product_pick_con_ids = fields.Many2many('product.move_service')

