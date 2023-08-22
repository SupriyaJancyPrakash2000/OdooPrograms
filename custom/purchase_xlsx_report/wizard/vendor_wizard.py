from odoo import fields,models

class ExcelWizard(models.TransientModel):
    _name= "purchase.wizard.xlsx"
    

    date_from = fields.Date(string="Date From")
    date_to = fields.Date(string="Date To")

    def action_new_excel(self):
        data={
      
            }
        return self.env.ref('purchase_xlsx_report.report_invoicing_xlsx_id').report_action(self, data=data)