from datetime import datetime
import json

from odoo import models, _
from odoo.exceptions import ValidationError


class SaleReportExcel(models.AbstractModel):
    _name = "report.bi_sale_report.xlsx_sale_report"
    _inherit = "report.report_xlsx.abstract"

    def generate_xlsx_report(self, workbook, data, lines):
        header_format = workbook.add_format(
            {
                "font_size": 10,
                "align": "center",
                "text_wrap": True,
                "valign": "vcenter",
                "font_name": "Calibri",
                "border": 1,
                "bold": True,
            }
        )
        format1 = workbook.add_format({"font_size": 11, "align": "center", "bg_color": "#A7ABBE", "border": 1})
        worksheet = workbook.add_worksheet("Sale Report")
        worksheet.write("A1", "Sl No.", header_format)
        worksheet.write("B1", "Order Date", header_format)
        worksheet.write("C1", "Order No.", header_format)
        worksheet.write("D1", "Customer", header_format)
        worksheet.write("E1", "Product", header_format)
        worksheet.write("F1", "Quantity", header_format)
        worksheet.write("G1", "Price Unit", header_format)
        worksheet.write("I1", "Subtotal", header_format)

        row = 2

        date_from = datetime.strptime(data["form"]["date_from"], "%Y-%m-%d")
        date_to = datetime.strptime(data["form"]["date_to"], "%Y-%m-%d")

        sale_order_line_ids = self.env["sale.order.line"].search(
            [
                ("order_id.state", "=", "sale"),
                ("order_id.date_order", ">=", date_from),
                ("order_id.date_order", "<=", date_to),
            ],
            order="date_order",
        )
        sl_no = 1
        for line in sale_order_line_ids:
            worksheet.write("A%s" % row, sl_no,format1)
            worksheet.write("B%s" % row, str(line.order_id.date_order.strftime("%d-%b-%Y")) if line.order_id.date_order else "",format1)
            worksheet.write("C%s" % row, line.order_id.name,format1)
            worksheet.write("D%s" % row, line.order_id.partner_id.name,format1)
            worksheet.write("E%s" % row, line.product_id.name,format1)
            worksheet.write("F%s" % row, line.product_qty,format1)
            worksheet.write("G%s" % row, line.unit_price,format1)
            worksheet.write("H%s" % row, line.price_subtotal,format1)
            sl_no+=1
            row += 1
