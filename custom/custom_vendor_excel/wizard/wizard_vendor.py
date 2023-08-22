from odoo import fields,models

class ExcelWizard(models.TransientModel):
    _name= "vendor.xlsx.wizard"
    

    date_from = fields.Date(string="Date From")
    date_to = fields.Date(string="Date To")
     
    def create_xlsx(self):
        data={
                'ids' : self.ids,
                'model' : self._name,
                'form':{
                    'date_from' : self.date_from,
                    'date_to' : self.date_to
                }
            }
        return self.env.ref('custom_vendor_excel.report_excel_xlsx_id').report_action(self,data=data)







