from odoo import fields, models


class CustomCrmReport(models.TransientModel):
    _name = "custom.crm.report"
    _description = "Custom CRM Report"

    date_from = fields.Date(string="Date From", required=True)
    date_to = fields.Date(string="Date To", required=True)
    sales_person = fields.Many2one('res.users', string="Salesperson")

    def generate_report(self):

        data = {
            "ids": self.ids,
            "model": self._name,
            "form": {
                "date_from": self.date_from,
                "date_to": self.date_to,
                "sales_person": self.sales_person,
            },
        }
        print("hiiiiiiiiiiiiiii")
        return self.env.ref("bi_crm_excel.action_openacademy_crmpipelinexlsx_report").report_action(self, data=data)
