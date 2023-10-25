from odoo import fields,models,api

class PayrollRule(models.Model):
    _inherit = "hr.payslip"

    @api.depends('employee_id', 'contract_id', 'struct_id', 'date_from', 'date_to')
    def _compute_input_line_ids(self):
        search_rec=False
        to_add_vals=[]
        res = super(PayrollRule, self)._compute_input_line_ids()
        for each in self:
            if each.employee_id:
                employee = each.employee_id
                
                date_from = each.date_from if each.date_from else date_from
                date_to = each.date_to if each.date_to else date_to
                search_rec = self.env['loan.payroll'].search([('emp_id', '=', self.employee_id.id)])
            if search_rec:
                    for lines in search_rec.loan_lines: 
                        existing_rule = each.struct_id.rule_ids.filtered(lambda x: x.code == "LD100")
                        if existing_rule:
                            if lines.date <= date_to and lines.date >= date_from:
                                input_type_id = self.env['hr.payslip.input.type'].search([('code', '=', "LD100")], limit=1)
                                to_add_vals = [(0, 0, {
                                        'amount': -(lines.amount),
                                        'input_type_id': input_type_id.id,
                                        'name': "Loan - %s" % (lines.date.strftime('%d/%m/%Y')),
                                    })]
                    input_line_vals = to_add_vals
                    each.update({'input_line_ids': input_line_vals})
        return res