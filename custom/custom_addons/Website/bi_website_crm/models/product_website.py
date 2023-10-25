from odoo import fields, models, http

class ProductLead(models.Model):
    _name = "product.info"

    service_name = fields.Char(string="Service Name")
    type = fields.Char(string="Product Type")
    is_published = fields.Boolean(string="Ready to Publish",default=False)

    def product_show(self):
        current_website = http.request.env['website'].get_current_website()
        if current_website:
            return {
                'type': 'ir.actions.act_url',
                 'url': '/service',
                'target': 'new'
            }
        else:
            print("No current website found!!!")

