from odoo import models,fields,api,_ 
from odoo.exceptions import UserError, ValidationError 

class LeaveRequest(models.Model):
    _inherit = 'hr.leave'

    def action_approve(self):
        existing_leave = self.env['hr.leave'].search([('employee_id.id', '=', self.employee_id.id)])
        new_rec = existing_leave.filtered(lambda rec:rec.date_from.month == self.date_from.month)

        if len(new_rec)>1:
            raise UserError(("An employee is allowed only one leave per month."))
        return super().action_approve()