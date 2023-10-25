from odoo import models, fields, api

class TaxDeductionEmployee(models.Model):
    _inherit = "hr.payslip"

    @api.depends('employee_id', 'contract_id', 'struct_id', 'date_from', 'date_to')
    def _compute_input_line_ids(self):
        res = super(TaxDeductionEmployee, self)._compute_input_line_ids()
        for payslip in self:
            if payslip.employee_id:
                emp = payslip.employee_id
                rec = self.env['hr.contract'].search([('employee_id','=',emp.id)])
                existing_rule = payslip.struct_id.rule_ids.filtered(lambda x: x.code == "TDS")
                if existing_rule:
                    input_types_id = self.env['hr.payslip.input.type'].search([('code', '=', 'TDS')], limit=1)
                    to_add_vals = [(0, 0, {
                        'amount': rec.tds_slab,
                        'input_type_id': input_types_id.id,
                        'name': 'TDS',
                    })]
                    payslip.write({'input_line_ids': to_add_vals})

        return res