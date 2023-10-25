from odoo import fields,models,api

class EmployeeSalaryInfo(models.Model):
    _inherit = "hr.applicant"

    emp_salary_sheet_ids = fields.One2many('salary.info.employee', 'employee_salary_sheet_id')
    wage = fields.Float(string="Wage")

    # def write(self, vals):
    #     res = super(EmployeeSalaryInfo, self).write(vals)
    #
    #     return res

    @api.onchange('stage_id')
    def create_product_variant_line(self):
        stage = self.env['hr.recruitment.stage'].search([('name', '=', 'Contract Signed')])
        if self.stage_id.id == stage.id:
            print("2222222222222222222222")
            variant_lines = []
            company_rules = self.env['emp.salary.rules'].search([])
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            for rec in company_rules:
                amount = (rec.perc/100)*self.wage
                if rec.name == 'Net Salary':
                    record = self.env['emp.salary.rules'].search([('categ_id', '=', 'Deduction')])
                    total_ded = sum(record.mapped('perc'))
                    print("-----------------------------", total_ded)
                    ded_salary = (total_ded / 100) * self.wage
                    amount = self.wage-ded_salary
                new_line = self.env['salary.info.employee'].create({
                    'name': rec.name,
                    'quant': 1,
                    'rate': rec.perc,
                    'amount': amount,
                    'category': rec.categ_id.id
                })
                variant_lines.append(new_line.id)
            self.emp_salary_sheet_ids = [(6, 0, variant_lines)]




class SalaryInfo(models.Model):
    _name = "salary.info.employee"

    employee_salary_sheet_id = fields.Many2one("hr.applicant")
    name = fields.Char(string="Name")
    quant = fields.Float(string="Quantity")
    rate = fields.Float(string="Rate%")
    amount = fields.Float(string="Amount")
    category = fields.Many2one('hr.salary.rule.category', string="Category")
