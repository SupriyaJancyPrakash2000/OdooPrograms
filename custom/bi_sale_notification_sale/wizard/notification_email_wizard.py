from odoo import fields,models 

class ApproveNotificationEmail(models.TransientModel):
    _name= "sale.approve.wizard"

    user = fields.Many2one('res.users',string="User")
    sale_id = fields.Many2one('sale.order',string="Sale")
    

    def approve_sale(self):
        self.env['mail.activity'].create({
            'user_id':self.user.id,
            'res_id':self.sale_id.id,
            'res_model_id':self.env.ref('sale.model_sale_order').id,
            'activity_type_id':4
        })

        body = "This is Demo!!"
        vals = {
            'subject':'Activity Alert',
            'body_html':body,
            'email_to':self.user.email,
            'email_from':self.env.user.email,
        }
        mail_id = self.env['mail.mail'].create(vals)
        mail_id.send()
    