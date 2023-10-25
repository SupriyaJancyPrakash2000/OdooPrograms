from dateutil.relativedelta import relativedelta
from datetime import date
from odoo import models, fields, api

class AttendanceOvertime(models.Model):
    _inherit = 'hr.payslip'


    @api.depends('employee_id', 'contract_id', 'struct_id', 'date_from', 'date_to')          
    def _compute_input_line_ids(self):
        res = super(AttendanceOvertime, self)._compute_input_line_ids()
        
        for each in self:
            if each.employee_id:
                employee = each.employee_id
                att_obj = self.env["hr.attendance"].search([
                    ("employee_id", "=", employee.id),
                    ("check_out", ">=", each.date_from),
                    ("check_in", "<=", each.date_to),
                ])
                if att_obj:
                    existing_rule = each.struct_id.rule_ids.filtered(lambda x: x.code == "OVR")
                    to_add_vals = [] 
                    avg_day_salary = 0
                    overtime_hours = 0
                    date_field_new = each.date_from  
                    while (date_field_new <= each.date_to):
                        rec = self.env["hr.attendance"].search([("employee_id", "=", employee.id)])
                        new_rec = rec.filtered(lambda x: x.check_out.date() == date_field_new)
                        sum_data = 0 
                        for att in new_rec:
                            sum_data += att.worked_hours
                        if sum_data > 8:
                            overtime_hours += sum_data - 8  
                                
                        date_field_new += relativedelta(days=1)
                    hike = 0
                    for lake in self.worked_days_line_ids:
                        if lake.work_entry_type_id.id == 1:        
                            avg_day_salary = (self.normal_wage / lake.number_of_days) / 8
                            hike = overtime_hours * avg_day_salary

                    if existing_rule:
                        rev_input_type_id = self.env['hr.payslip.input.type'].search([('code', '=', "OVR")], limit=1)
                        to_add_vals.append((0, 0, {
                            'amount': hike,
                            'input_type_id': rev_input_type_id.id,
                            'name': "Overtime Bonus"
                        }))
                        input_line_vals = to_add_vals
                        each.update({'input_line_ids': input_line_vals})
                else:
                  
                    each.update({'input_line_ids': []})
        return res
        
                
    
        