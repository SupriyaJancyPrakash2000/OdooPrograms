from odoo import fields, models


class CustomSaleReport(models.TransientModel):
    _name = "custom.sale.report"
    _description = "Custom Sale Report"

    date_from = fields.Date(
        string="Date From",
        required=True,
    )
    date_to = fields.Date(
        string="Date To",
        required=True,
    )

    def generate_report(self):
        data = {
            "ids": self.ids,
            "model": self._name,
            "form": {
                "date_from": self.date_from,
                "date_to": self.date_to,
            },
        }
        return self.env.ref("bi_sale_report.action_custom_sale_report").report_action(self, data=data, config=False)
