from datetime import datetime, date, timedelta
from odoo import fields,api,models

class LopWorkedDays(models.Model):
    _inherit = 'hr.payslip'

    @api.depends('employee_id', 'contract_id', 'struct_id', 'date_from', 'date_to')
    def _compute_worked_days_line_ids(self, domain=None):

        res = super(LopWorkedDays, self)._compute_worked_days_line_ids()


        to_add_vals = []
        for each in self:
            if each.employee_id:
                employee = each.employee_id
                records = self.env['hr.leave'].search(
                    [('employee_id', '=', employee.id),
                     ('date_from', '<=', self.date_to),
                     ('date_to', '>=', self.date_from),
                     ('holiday_status_id', '=', 6),
                     ('state', '=', 'validate')])
                print("???????????????????", records)
                lop = len(records)
                print(":::::::::::::::::::", lop)

                work_entry_type = self.env['hr.work.entry.type'].search([('code', '=', 'LV80')])
                if work_entry_type:

                    to_add_vals = [(0, 0, {
                        'sequence': 27,
                        'work_entry_type_id': work_entry_type.id,
                        'number_of_days': lop,
                        'number_of_hours': lop*8,
                    })]
            worked_line_vals = to_add_vals
            each.update({'worked_days_line_ids': worked_line_vals})
        return res


    # @api.depends('is_paid', 'number_of_hours', 'payslip_id', 'contract_id.wage', 'payslip_id.sum_worked_hours')
    # def _compute_amount(self):
    #
    #     res = super(LopWorkedDays, self)._compute_amount()
    #     print("aaaaaaaaaaaaaaaaaaaaaaaaammmmmmmmmm")
    #     work_entry_type = self.env['hr.work.entry.type'].search([('code', '=', 'LV80')])
    #     for worked_days in self:
    #         if worked_days.work_entry_type_id == work_entry_type.id:
    #             worked_days.amount = 100
    #     return res





