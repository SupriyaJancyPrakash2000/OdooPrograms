from dateutil.relativedelta import relativedelta
from odoo import models,fields,api

class LoanAllocation(models.Model):
    _name = 'loan.sanction'

    emp_id = fields.Many2one('hr.employee',string="Employee")
    instal = fields.Integer(string="Number of Installment")
    check = fields.Boolean(default=False)
    installment = fields.Integer(string="installment")
    date = fields.Date(string="Date")
    loan_lines = fields.One2many('loan.sanctionlines','lines_id')
    state = fields.Selection([
        ('draft','Draft'),
        ('approve','Approved')
    ],
    default='draft')
    

    
    def loan_sanction(self):
        self.check = True
        records = self.env['employee.loan'].search([('emp_id', '=', self.emp_id.id)])
        total_amount = 0
        for rec in records:
            total_amount += rec.amt
        value = total_amount/self.instal
        self.installment = value

    def loan_approval(self):
        # global last_date
        newloan_lines=[]
        self.write({'state':'approve'})
        total_amount = sum(self.loan_lines.mapped("amount"))
        current_date = self.date
        if self.loan_lines:
            sum_of_amt = 0
            for each in self.loan_lines:
                if each.paid == True:
                    sum_of_amt += each.amount
                    last_date = each.date
            new_amount = total_amount-sum_of_amt
            if self.instal:
                split_new = new_amount/self.instal
            else:
                split_new = 0
            for line in self.loan_lines:
                if line.paid:
                    new_line = self.env['loan.sanctionlines'].create({
                    'date':current_date,
                    'amount':line.amount,
                    'paid':True
                })
                current_date = current_date+relativedelta(months=1)
                newloan_lines.append(new_line.id)
            last_date_1 = last_date + relativedelta(months=1)
            for each in range(self.instal):
                new_line = self.env['loan.sanctionlines'].create({
                    'date':last_date_1,
                    'amount':split_new
                })
                last_date_1 = last_date_1+relativedelta(months=1)
                newloan_lines.append(new_line.id)
            
            self.loan_lines = [(6, 0, newloan_lines)]


        else:
            newloan_lines=[]
            records = self.env['employee.loan'].search([('emp_id', '=', self.emp_id.id)])
            total_amount = 0
            for rec in records:
                total_amount += rec.amt
            if self.instal: 
                split = total_amount/self.instal
            else:
                split = 0
            current_date = self.date
            for each in range(self.instal):
                new_line = self.env['loan.sanctionlines'].create({
                    'date':current_date,
                    'amount':split
                })
                current_date = current_date+relativedelta(months=1)
                newloan_lines.append(new_line.id)
            self.loan_lines = [(6, 0, newloan_lines)]


        



    # @api.onchange('instal')
    # def generate_loan_lines(self):
    #     newloan_lines=[]
    #     records = self.env['employee.loan'].search([('emp_id', '=', self.emp_id.id)])
    #     total_amount = 0
    #     for rec in records:
    #         total_amount += rec.amt
    #     if self.instal: 
    #         split = total_amount/self.instal
    #     else:
    #         split = 0
    #     current_date = self.date
    #     for each in range(self.instal):
    #         new_line = self.env['loan.sanctionlines'].create({
    #             'date':current_date,
    #             'amount':split
    #         })
    #         current_date = current_date+relativedelta(months=1)
    #         newloan_lines.append(new_line.id)
    #     self.loan_lines = [(6, 0, newloan_lines)]


    def state_back(self):
        self.write({'state':'draft'})
        # lines = self.env['loan.sanctionlines'].search([])
        # for line in lines:
        #     if line.paid == False:
        #         line.unlink()

class LoanAllocationLine(models.Model):
    _name="loan.sanctionlines"

    lines_id = fields.Many2one('loan.sanction')
    date = fields.Date()
    amount = fields.Integer(string="Amount")
    paid = fields.Boolean() 


