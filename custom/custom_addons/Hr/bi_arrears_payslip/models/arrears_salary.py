from odoo import fields, models, api
from datetime import date, timedelta, datetime

class EmployeeArrears(models.Model):
    _inherit = "hr.payslip"

    @api.depends('employee_id', 'contract_id', 'struct_id', 'date_from', 'date_to')
    def _compute_input_line_ids(self):


        arrears = 0
        to_add_vals = []
        res = super(EmployeeArrears, self)._compute_input_line_ids()
        for each in self:
            if each.employee_id:
                employee = each.employee_id
                date_from = each.date_from if each.date_from else date_from
                date_to = each.date_to if each.date_to else date_to


                month_date_from = date_from.strftime('%m')
                print("<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>", month_date_from)

                rec = self.env['salary.arrears'].search([('employee_id', '=', employee.id)])

                if rec.arrears_boolean == True:
                    print("hiiiiiiiiiii")
                    employee = self.env['hr.contract'].search([('employee_id', '=', self.employee_id.id)])

                    wage = employee.wage
                    amount = rec.salary
                    # hike = wage + amount
                    employee.update({'wage': amount})

                if rec.arrears_boolean != True:
                    date_of_arr = rec.effective_from_month
                    print("......................................", date_of_arr)
                    month_date_from_arr = date_of_arr.strftime('%m')
                    print("<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>", month_date_from_arr)
                    payslip_month = int(month_date_from)
                    arrears_month = int(month_date_from_arr)

                    print(";;;;;;;;;;;;;;;;;;;;;",arrears_month)
                    print(";______________________",rec.arrear_amount)

                    if arrears_month == payslip_month:
                        arrears = rec.arrear_amount
                    else:
                        month_dif = payslip_month-arrears_month
                        arrears = (month_dif+1)*rec.arrear_amount

                        print("]]]]]]]]]]]]]]]]]]]]]]]]]]", arrears)


                    existing_rule = each.struct_id.rule_ids.filtered(lambda x: x.code == "ARS")
                    if existing_rule:
                        print("@@@@@@@@@@@@@@@@@@@")
                        input_type_id = self.env['hr.payslip.input.type'].search([('code', '=', "ARS")], limit=1)
                        to_add_vals = [(0, 0, {
                            'amount': arrears,
                            'input_type_id': input_type_id.id,
                            'name': "ARS",
                        })]
                        input_line_vals = to_add_vals
                        each.update({'input_line_ids': input_line_vals})
                        rec.arrears_boolean = True

                else:

                    existing_rule = each.struct_id.rule_ids.filtered(lambda x: x.code == "ARS")
                    if existing_rule:
                        print("^^^^^^^^^^^^^^^")
                        input_type_id = self.env['hr.payslip.input.type'].search([('code', '=', "ARS")], limit=1)
                        to_add_vals = [(0, 0, {
                            'amount': 0.0,
                            'input_type_id': input_type_id.id,
                            'name': "ARS",
                        })]
                        input_line_vals = to_add_vals
                        each.update({'input_line_ids': input_line_vals})
                        rec.arrears_boolean = True


                        # employee = self.env['hr.contract'].search([('employee_id', '=', self.employee_id.id)])
                        # wage = employee.wage
                        # amount = rec.arrear_amount
                        # hike = wage + amount
                        # employee.update({'wage': hike})

                    # if len(self.input_line_ids) > 0:
                    #     print("******************")
                    #     (self.input_line_ids =  Fsalcgf
                    #     each.update({'input_line_ids': [(5, 0, 0)]})
        return res









