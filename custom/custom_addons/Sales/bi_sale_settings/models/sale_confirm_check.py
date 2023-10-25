from odoo import fields, models, api, exceptions
from dateutil.relativedelta import relativedelta
import datetime


class SaleConfirmCheck(models.Model):
    _inherit = 'sale.order'

    @api.constrains('validity_date')
    def _check_expiration_date(self):
        if self.validity_date:
            sale_date = self.date_order.date()
            print('>>>>>>>>>>>>', sale_date)
            no_of_day = int(self.env['ir.config_parameter'].sudo().get_param('no_of_days.no_of_days'))

            # for i in range(1, no_of_day + 1):
            sale_date = sale_date + relativedelta(days=no_of_day)

            if sale_date > self.validity_date:
                raise exceptions.UserError("Expiration limit is exceeded!!!!")

