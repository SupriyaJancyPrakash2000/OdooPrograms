from odoo import models,fields,api

class ExcelWizard(models.TransientModel):
    _name= "sales.excel.wizard"
    

    date_from = fields.Date(string="Date-from")
    date_to = fields.Date(string="Date-to")
    sales_person_id = fields.Many2one('res.users', string="Sales person")

    def create_excel(self):
        data={
            'ids' : self.ids,
            'model' : self._name,
            'form':{
                'date_from' : self.date_from,
            'date_to' : self.date_to,
            # 'sales_person_id' : self.sales_person_id.id,
            }
            }
        return self.env.ref('custom_sale_excel.report_excel_xlsx').report_action(self,data=data)


