from odoo import models, api, exceptions


class CheckRatio(models.Model):
    _inherit = 'mrp.bom'

    @api.constrains('bill_mat_line_ids')
    def _check_ratio(self):
        sum_of_ratio = 0
        for lines in self.bill_mat_line_ids:
            sum_of_ratio += lines.ratio
        if sum_of_ratio > 100:
            raise exceptions.UserError("The sum of ratio must be greater than 100!!")