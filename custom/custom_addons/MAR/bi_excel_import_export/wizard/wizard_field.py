from odoo import fields, models, api, _
import xlrd
import base64
from odoo.exceptions import UserError


class ViewWizard(models.TransientModel):
    _name = "excel.wizard"

    file_upload = fields.Binary(string="File Upload")
    mrp_id = fields.Many2one('mrp.bom', string="mrp")

    def export_excel(self):
        return self.env.ref('bi_excel_import_export.mrp_report_excel_xlsx_id').report_action(self)

    def import_excel(self):
        for record in self:
            if record.file_upload:
                workbook = xlrd.open_workbook(file_contents=base64.decodebytes(record.file_upload))
                sheet = workbook.sheet_by_index(0)

                bom = self.env["mrp.bom"].browse(self.mrp_id.id)

                for row in range(1, sheet.nrows):
                    line_values =[]
                    product_name = sheet.cell(row, 0).value  # Assuming the product is identified by name
                    quantity = sheet.cell(row, 1).value

                    product = self.env["product.product"].search([('name', '=', product_name)], limit=1)
                    if product:
                        line = (0, 0, {
                            'product_id': product.id,
                            'product_qty': quantity,
                        })
                        line_values.append(line)

                        self.mrp_id.bom_line_ids = line_values

                    else:
                        raise UserError(f"Product with name '{product_name}' not found.")

                print("Data imported successfully")
            else:
                raise UserError("No file selected")

















