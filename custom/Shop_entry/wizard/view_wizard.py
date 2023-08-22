from odoo import fields,models,api,_

class ViewWizard(models.TransientModel):
    _name= "sales.shop.wizard"
    

    product_id = fields.Many2one('product.product',string="Product")
    checklist = fields.Boolean(string="Check List")
    value = fields.Float(string="Value")
    sales_id = fields.Many2one('sales.shop',string="Sale")
    product_ids = fields.Many2many('product.product',string="Products")
    invoices_view_ids = fields.Many2many("account.move",string="Invoice")


    def pass_value(self):
        sale_shop = self.env['sales.shop'].search([('id','=',self.sales_id.id)])
        for lines in sale_shop.sales_shop_line:
            if lines.product_id.id == self.product_id.id:
                lines.amount = self.value
        
    def delete_product(self):
        # sale_shop = self.env['sales.shop'].search([('id','=',self.sales_id.id)])
        for lines in self.sales_id.sales_shop_line:
            if lines.product_id.id == self.product_id.id:
                lines.unlink()

    @api.onchange('checklist')
    def onchange_manytoone(self):
        record = self.env['sales.shop'].search([('id','=',self.sales_id.id)])
        product_list=[]
        for lines in record.sales_shop_line:
            product_list.append(lines.product_id.id)
        return {
            'domain': {
                'product_id':[('id', 'in', product_list)]
            }
        }
#invisible the value field in wizard
    # @api.onchange('product_ids')
    # def iterate_product_ids(self):
    #     count = 0
    #     for each in self.product_ids:
    #         count+= 1
    #     if(count%2 == 0):
    #         self.checklist = True
    #     else:
    #         self.checklist = False

#make value as readonly field
    @api.onchange('product_id', 'product_ids')
    def onchange_product_id(self):
        self.checklist = False 
        if self.product_id.id in self.product_ids.ids:
            self.checklist = True
            
    @api.onchange('product_id', 'product_ids')
    def onchange_product_check(self):
        search = self.env['product.product'].search(([]))
        search.product_check = False
        if self.product_id.id in self.product_ids.ids:
            # rec = search.search([('id','=',self.product_id.id)])
            # rec.product_check = True
            self.product_id.product_check = True

    def invoice_pass(self):
        # for each in self.invoices_view_ids.ids:
        #     invoice_list.append(each)
        invoice_list = self.invoices_view_ids.ids
        self.sales_id.invoice_ids = invoice_list
        
        self.sales_id.sales_shop_line.checkbox = False
        for rec in self.invoices_view_ids:
            for line in self.sales_id.sales_shop_line:
                if line.checkbox == False:
                    line.line_invoice_ids = rec
                    line.checkbox = True
                    break
            

        






    
            
        
        
   
        