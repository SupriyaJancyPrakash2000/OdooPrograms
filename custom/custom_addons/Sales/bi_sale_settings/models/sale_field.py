from odoo import fields,models,api



class SaleSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    no_of_days = fields.Integer(string="Number of Days", config_parameter="no_of_days.no_of_days")

    def set_values(self):
        res = super(SaleSettings, self).set_values()
        number_of_days = self.env['ir.config_parameter'].sudo()
        number_of_days.set_param('no_of_days.no_of_days', self.no_of_days)
        return res

