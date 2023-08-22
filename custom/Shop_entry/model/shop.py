from odoo import api, fields, models, _

class ShopEntry(models.Model):
    _name= "sales.shop"
    _rec_name= "id"


    shop_name = fields.Char(string="Shop Name")
    place = fields.Char(string="Place") 
    amount = fields.Float(string="Amount")
    count = fields.Integer(string="Count")
    change = fields.Float(string="Change")
    sales_shop_line = fields.One2many('sales.shop.line','sales_shop_line_id')
    total_line = fields.Integer(string="Total Line", compute="compute_total_line_form")
    sales_id = fields.Many2one("sale.order",string="Sale")
    product_count = fields.Integer(compute="compute_product_count",string="Product count")
    customer_id = fields.Many2one("res.partner",string="Customer")
    invoice_id = fields.Many2one("account.move",string="Invoice") 
    invoice_count = fields.Integer(compute="compute_invoice_count",string="Invoice count")
    invoice_view_ids = fields.Many2many("account.move",string="Invoice View",compute="compute_manytomany")
    invoice_ids = fields.Many2many("account.move",string="Invoices")
    #sequence
    reference_no = fields.Char(string='Shop Reference', required=True,
                          readonly=True, default=lambda self: ('New'))
    desired_name = fields.Char(string="Name")
    checkbox = fields.Boolean() 
    
    #sequence creation
    # @api.model
    # def create(self, vals):
    #     if vals.get('reference_no', _('New')) == _('New'):
    #         vals['reference_no'] = self.env['ir.sequence'].next_by_code(
    #        'shop.sequence') or _('New')
    #     res = super(ShopEntry, self).create(vals)
    #     return res
    
    #Sequence creation using customized button
    def create_sequence(self):
        sequence = self.env['ir.sequence'].next_by_code('shop.sequence')
        if self.checkbox == False:
            if self.desired_name:
                sequence_code = self.desired_name[0:3]+'\\'
                self.reference_no = sequence_code + sequence or 'New'
                self.checkbox = True
        
    @api.onchange('count','amount')
    def count_sales_shop_line(self):
        shop_lines = []
        month_list = ['January','February','March','April','May','June','July','August','September','October','November','December']
        # new_amount = (self.amount)/(self.count)
        new_amount = self.amount
        sumofamount = 0
        for rec in range(self.count):
            new_line = self.env['sales.shop.line'].create({
                    'month': month_list[rec % 12],
                    'amount': new_amount
                    })
            shop_lines.append(new_line.id)
            sumofamount = sumofamount+new_amount
            new_amount = (new_amount)-((10/100)*new_amount)
            
        self.sales_shop_line = [(6, 0, shop_lines)]
        self.change = sumofamount

    # @api.onchange('sales_shop_line')
    # def onchange_change_field(self):
    #     total_amount = 0
    #     for line in self.sales_shop_line:
    #         total_amount = total_amount+line.amount
    #     self.change = total_amount

 #save button  
    # def write(self, vals):
    #     total_amount = 0
    #     for line in self.sales_shop_line:
    #         total_amount += line.amount
    #     vals['change'] = total_amount
    #     return super(ShopEntry,self).write(vals)

    #button Box
    def sale_order_view(self):
        self.ensure_one()
        return {
                'type': 'ir.actions.act_window',
                'name': 'Sale view',
                'view_mode': 'tree,form',
                'res_model': 'sale.order',
                'domain': [('id', 'in', self.sales_id.ids)],
                'context': "{'create': False}"
            }
    
    def compute_total_line_form(self):
        count_line = 0
        sale_shop = self.env['sales.shop'].search(([]))
        for rec in sale_shop.sales_shop_line:
            count_line += 1 
        sale_shop.total_line = count_line

    @api.depends('sales_id')
    def compute_product_count(self):
        count_line = self.env['sale.order.line'].search_count([('order_id', '=',self.sales_id.id)])
        self.product_count = count_line

    def create_invoice(self):
        invoice_lines = []
        for line in self.sales_shop_line:
                invoice_lines.append(fields.Command.create({
                    'product_id': line.product_id.id,
                    'name': line.product_id.name,
                    'quantity': 1,
                    'price_unit': line.amount,
                }))

        invoice_vals = {
                'partner_id': self.customer_id.id,
                'invoice_line_ids': invoice_lines,
                'invoice_id':self.id,
                'move_type': 'out_invoice',
                }

        invoice = self.env['account.move'].create(invoice_vals)

        #perform confirm invoice
        if invoice:
            invoice.action_post()
        
        return {
                "name": _("Account Moves"),
                "type": "ir.actions.act_window",
                "view_mode": "form",
                "res_model": "account.move",
                "res_id": invoice.id,
            }
    
    #many2many field is replaced with created invoices using compute function
    def compute_invoice_count(self):
        invoice_search = self.env['account.move'].search_count([('invoice_id','=',self.id)])
        self.invoice_count = invoice_search

    #button box Invoice Count
    def invoice_view(self):
        self.ensure_one()
        return {
                'type': 'ir.actions.act_window',
                'name': 'Account view',
                'view_mode': 'tree,form',
                'res_model': 'account.move',
                'domain': [('invoice_id', '=', self.id )],
                'context': "{'create': False}"
            }

    def compute_manytomany(self):
        records = self.env['account.move'].search([('invoice_id','=',self.id)])
        self.write({
            "invoice_view_ids":[(6,0,records.ids)]
        })

    def create_wizard(self):
        # action = self.env.ref('Shop_entry.action_view_wizard').read()[0]
        # return action
        product_list=[]
        for lines in self.sales_shop_line:
            product_list.append(lines.product_id.id)
        invoice_list = []
        for each in self.invoice_view_ids.ids:
            invoice_list.append(each)

        return {
            'name': _("create wizard"),
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'sales.shop.wizard',
            'target': 'new',
            #pass id to wizard
            'context': {    
                'default_sales_id': self.id,
                'default_product_ids':[(4,x)for x in product_list],
                'default_invoices_view_ids':[(4,x)for x in invoice_list],
                }
        }
        
   

        
class ShopOrderLine(models.Model):
    _name= "sales.shop.line"

    sales_shop_line_id = fields.Many2one("sales.shop")
    month = fields.Char(string="Month")
    amount = fields.Float(string="Amount")
    product_id = fields.Many2one("product.product", string="Product",domain="[('checklist','=',True)]")
    line_invoice_ids = fields.Many2many('account.move',string="Invoces") 
    checkbox = fields.Boolean()    


    

    

