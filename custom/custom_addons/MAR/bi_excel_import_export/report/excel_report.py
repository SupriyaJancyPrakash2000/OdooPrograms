from odoo import models


class PartnerXlsx(models.AbstractModel):
    _name = 'report.bi_excel_import_export.mrp_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, partners):

        sheet = workbook.add_worksheet("vendor bill report")
        bold = workbook.add_format({'bold': True, 'align': 'center', 'border': True})
        center_align = workbook.add_format({'align': 'center'})
        left_align = workbook.add_format({'align': 'left'})


        sheet.write('A1', 'Component', bold)
        sheet.write('B1', 'Quantity', bold)


        sheet.set_column('A:A', 20, center_align)
        sheet.set_column('B:B', 13, center_align)





















