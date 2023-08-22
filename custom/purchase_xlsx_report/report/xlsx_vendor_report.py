from odoo import models

class PartnerXlsx(models.AbstractModel):
    _name = 'report.purchase_xlsx_report.excel_take'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
        sheet = workbook.add_worksheet("vendor bill report")
        bold = workbook.add_format({'bold': True, 'align':'center', 'border': True})
        center_align = workbook.add_format({'align': 'center'})
        left_align = workbook.add_format({'align': 'left'})

        sheet.merge_range('A1:D1', 'PRODUCT DETAILS XLSX', bold)
        sheet.write('A2', 'Sl.No', bold)
        sheet.write('B2', 'Product name', bold)
        sheet.write('C2', 'Quantity', bold)
        sheet.write('D2', 'Subtotal', bold)

        sheet.set_column('A:A', 13, center_align)
        sheet.set_column('B:B', 45, left_align)
        sheet.set_column('C:C', 20, center_align)
        sheet.set_column('D:D', 20, center_align)

        purchase_rec = self.env['purchase.order'].search([])
        row = 3
        serial_number = 1
         
        product_dic = {}
        for each in purchase_rec:
            for i in each.order_line:
                if i.product_id.name not in product_dic:
                    product_dic[i.product_id.name] = { 
                        'Quantity': 0.0,
                        'Subtotal': 0.0,
                    }
                product_dic[i.product_id.name]['Quantity'] += i.product_qty
                product_dic[i.product_id.name]['Subtotal'] += i.price_subtotal 

        for i.product_id.name, totals in product_dic.items():
            if any(totals.values()):
                sheet.write("A%s" % row, serial_number)
                serial_number +=1 
                sheet.write("B%s" % row, i.product_id.name)
                sheet.write("C%s" % row, totals['Quantity'])
                sheet.write("D%s" % row, totals['Subtotal'])

                row += 1



                

