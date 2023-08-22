from odoo import fields,models

class AutoDelivery(models.Model):
    _inherit = 'sale.order'

    auto_delivery= fields.Boolean(string="Auto Delivery")

    def validate_delivery(self):
        delivery = self.env['stock.picking'].search([('sale_id', '=', self.id)], limit=1)
    
        for each in delivery:
            move_ids_list = []
            
            # Create a new picking type object based on your requirements
            # picking_type = self.env["stock.picking.type"].search([('id', '=', 2)], limit=1)
            
            for line in each.move_ids_without_package:
                if not line.quantity_done:
                    move_ids_list.append((0, 0, {
                        'product_id': line.product_id.id,
                        'product_uom_qty': line.product_uom_qty,
                        'quantity_done': line.quantity_done,  # Assuming quantity_done should be equal to product_uom_qty
                        'location_id': delivery.location_id.id,
                        'location_dest_id': delivery.partner_id.property_stock_customer.id,  # Use appropriate field to get the customer's stock location
                        'name': each.origin,
                        'product_uom':line.product_uom
                    }))
            
            new_picking = self.env['stock.picking'].create({
                'partner_id': each.partner_id.id,
                'location_id': each.location_id.id,
                'location_dest_id': each.partner_id.property_stock_customer.id,  # Use appropriate field to get the customer's stock location
                'origin': each.origin,
                "move_ids_without_package": move_ids_list,
                'sale_id': self.id,
                'picking_type_id': each.picking_type_id.id,
            })
            
            # Confirm the new picking and its stock moves
            
            new_picking.action_assign()
            new_picking.button_validate()
            new_picking.action_set_quantities_to_reservation()
            new_picking._action_done()
     

            
            
            # Mark the new picking as done
            
            