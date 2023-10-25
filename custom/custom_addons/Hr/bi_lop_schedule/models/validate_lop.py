from odoo import models, api, exceptions


class CheckLop(models.Model):
    _inherit = 'hr.leave'

    @api.constrains('request_date_from', 'request_date_to')
    def _check_lop(self):
        for leave in self:
            start_date = leave.request_date_from
            end_date = leave.request_date_to

            records = self.env['hr.leave'].search(
                [('employee_id', '=', self.employee_id.id),
                 ('date_from', '=', end_date),
                 ('date_to', '=', start_date),
                 ('state', '=', 'validate')])

            if records:
                raise exceptions.UserError("Already has LOP for this date range")