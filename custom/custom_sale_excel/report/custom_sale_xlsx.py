from odoo import models, _

class PartnerXlsx(models.AbstractModel):
    _name = 'report.custom_sale_excel.sale_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, partners):
        sheet = workbook.add_worksheet("sale order report")
        bold = workbook.add_format({'bold': True, 'align':'center', 'border': True})
        right_align = workbook.add_format({'align': 'right'})
        # title = workbook.add_format({'bold': True, 'align': 'center', 'font_size':10, 'border':True})
        date_from = data['form']['date_from']
        date_to = data['form']['date_to']
        # sale_person = data['form']['sales_person_id']
        # sale_order = self.env['sale.order'].search([('create_date','>=',date_from), ('create_date', '<=', date_to)])

        domain = []
        temp_value = 0

        if self.env.user.has_group('custom_sale_excel.overtime_managers_access_xlsx') or self.env.user.has_group('custom_sale_excel.overtime_users_access_xlsx'):
            if date_from:
                domain.append(('create_date', '>=', date_from))
            if date_to:
                domain.append(('create_date', '<=', date_to))
            if not self.env.user.has_group('custom_sale_excel.overtime_managers_access_xlsx'):
                domain.append(('user_id', '=', self.env.user.id))
            temp_value = 1
        
        if temp_value == 1:
            sale_orders= self.env['sale.order'].search(domain)
            row = 3
            serial_number = 1
            sheet.merge_range('A1:E1', 'SALE ORDER', bold)
            sheet.write('A2', 'Sl.No', bold)
            sheet.write('B2', 'Sale.No', bold)
            sheet.write('C2', 'Date', bold)
            sheet.write('D2', 'Amount', bold)

            for each in sale_orders:

                order_date = each.date_order
                date_d = order_date.strftime("%Y-%m-%D")
                sheet.write("A%s" % row, serial_number)
                sheet.set_column('A:A', 15, right_align)
                serial_number +=1
                sheet.write("B%s" % row, each.name)
                sheet.set_column('B:B', 17, right_align)
                sheet.write("C%s" % row, date_d)
                sheet.set_column('C:C', 20, right_align)
                sheet.write("D%s" % row, each.amount_total)
                sheet.set_column('D:D', 20, right_align)
                row += 1
        else:
            print()
       


             


