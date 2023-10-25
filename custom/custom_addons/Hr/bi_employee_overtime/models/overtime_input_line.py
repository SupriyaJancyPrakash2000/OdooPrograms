from odoo import fields,models,api 

class OvertimeWorkWage(models.Model):
    _inherit = "hr.payslip"

    @api.depends('employee_id', 'contract_id', 'struct_id', 'date_from', 'date_to')
    def _compute_input_line_ids(self):
        search_rec=False
        to_add_vals=[]
        avg_salary = 0
        extra = 0
        res = super(OvertimeWorkWage, self)._compute_input_line_ids()
        for each in self:
            if each.employee_id:
                employee = each.employee_id
                date_from = each.date_from if each.date_from else date_from
                date_to = each.date_to if each.date_to else date_to
                search_rec = self.env['employee.payroll'].search([('emp_id', '=', self.employee_id.id)])
                for line in self.worked_days_line_ids:
                    if line.work_entry_type_id.id == 1:
                        avg_salary = (self.normal_wage / line.number_of_days)/8
    
            if search_rec:
                    for lines in search_rec.loan_lines: 
                        existing_rule = each.struct_id.rule_ids.filtered(lambda x: x.code == "OTW")
                        if existing_rule:
                            sum_over_time = sum(search_rec.loan_lines.mapped('hours_worked')) * avg_salary
                            if lines.date <= date_to and lines.date >= date_from:
                                input_type_id = self.env['hr.payslip.input.type'].search([('code', '=', "OTW")], limit=1)
                                to_add_vals = [(0, 0, {
                                        'amount': sum_over_time,
                                        'input_type_id': input_type_id.id,
                                        'name': "overtime - %s" % (lines.date.strftime('%d/%m/%Y')),
                                    })]
                    input_line_vals = to_add_vals
                    each.update({'input_line_ids': input_line_vals})
            



    