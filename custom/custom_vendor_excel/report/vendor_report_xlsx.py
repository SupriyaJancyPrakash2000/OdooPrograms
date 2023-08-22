from odoo import models

class PartnerXlsx(models.AbstractModel):
    _name = 'report.custom_vendor_excel.vendor_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, partners):

        sheet = workbook.add_worksheet("vendor bill report")
        bold = workbook.add_format({'bold': True, 'align':'center', 'border': True})
        center_align = workbook.add_format({'align': 'center'})
        left_align = workbook.add_format({'align': 'left'})

        sheet.merge_range('A1:F1', 'VENDOR BILL DETAILS', bold)
        sheet.write('A2', 'Sl.No', bold)
        sheet.write('B2', 'Sale.No', bold)
        sheet.write('C2', 'Vendor Name', bold)
        sheet.write('D2', 'Amount', bold)
        sheet.write('E2', 'State', bold)
        sheet.write('F2', 'Paid', bold)
        sheet.set_column('A:A', 13, center_align)
        sheet.set_column('B:B', 45, center_align)
        sheet.set_column('C:C', 20, center_align)
        sheet.set_column('D:E', 20, center_align)
        sheet.set_column('F:F', 14, center_align)
        sheet.set_column('G:G', 14, center_align)

        
        date_from = data['form']['date_from']
        date_to = data['form']['date_to']

        vendor_rec =  self.env['account.move'].search([('move_type','=', 'in_invoice')])
        row = 3
        serial_number = 1
         

        for each in vendor_rec:

            if each.amount_residual == 0:
                pay_state = "Yes"
            else:
                pay_state = "No"

            sheet.write("A%s" % row, serial_number)
            serial_number +=1 
            sheet.write("B%s" % row, each.name,left_align)
            sheet.write("C%s" % row, each.partner_id.name)
            sheet.write("D%s" % row, each.amount_untaxed,left_align)
            sheet.write("E%s" % row, each.state)
            sheet.write("F%s" % row, pay_state)
            
            purchase_created = self.env['purchase.order'].search([('invoice_ids','=', each.id)])
            if purchase_created:
                sheet.write('G%s' % row, purchase_created.name)
            else:
                sheet.write('G%s' % row, "")

            for line in each.invoice_line_ids:
               
                row += 1
                sheet.write("B%s" % row, line.name)
                sheet.write("D%s" % row, line.price_unit)

            


            row += 1






       


             


