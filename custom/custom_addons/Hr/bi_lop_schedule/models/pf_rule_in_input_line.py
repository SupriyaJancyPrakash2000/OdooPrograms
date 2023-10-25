from odoo import fields, models, api



class EmployeePF(models.Model):
    _inherit = "hr.payslip"

    @api.depends('employee_id', 'contract_id', 'struct_id', 'date_from', 'date_to')
    def _compute_input_line_ids(self):
        # search_rec=False
        to_add_vals = []

        res = super(EmployeePF, self)._compute_input_line_ids()


        for each in self:

            if each.employee_id:
                employee = each.employee_id
                date_from = each.date_from if each.date_from else date_from
                date_to = each.date_to if each.date_to else date_to
                wage = sum(self.worked_days_line_ids.mapped("amount"))
                print("............................",wage)
                pf = ((12 / 100) * wage)
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",pf)

                existing_rule = each.struct_id.rule_ids.filtered(lambda x: x.code == "PF")
                if existing_rule:
                    input_type_id = self.env['hr.payslip.input.type'].search([('code', '=', "PF")], limit=1)
                    to_add_vals = [(0, 0, {
                        'amount': pf,
                        'input_type_id': input_type_id.id,
                        'name': "PF",
                    })]
            input_line_vals = to_add_vals
            each.update({'input_line_ids': input_line_vals})
        return res



