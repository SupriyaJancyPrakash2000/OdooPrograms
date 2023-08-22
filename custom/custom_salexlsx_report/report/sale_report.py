from odoo import models

class PartnerXlsx(models.AbstractModel):
    _name = 'report.custom_salexlsx_report.sale_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, partners):

        sheet = workbook.add_worksheet("vendor bill report")
        bold = workbook.add_format({'bold': True, 'align':'center', 'border': True})
        center_align = workbook.add_format({'align': 'center'})
        left_align = workbook.add_format({'align': 'left'})

        sheet.merge_range('A1:F1', 'SALE ORDER DETAILS', bold)
        sheet.write('A2', 'Sl.No', bold)
        sheet.write('B2', 'Sales Person', bold)
        sheet.write('C2', 'Sale Orders', bold)
        sheet.write('D2', 'Invoice', bold)
        sheet.write('E2', 'Total Amount', bold)
        sheet.write('F2', 'Paid Amount', bold)

        sheet.set_column('A:A', 13, center_align)
        sheet.set_column('B:B', 20, center_align)
        sheet.set_column('C:C', 50, left_align)
        sheet.set_column('D:F', 20, center_align)
        
        
        date_from = data['form']['date_from']
        date_to = data['form']['date_to']

        sale_rec = self.env['sale.order'].search([])
        row = 3
        serial_number = 1

        sale_person = sale_rec.mapped('user_id')

        for each in sale_person:
            filter_sale_order = sale_rec.filtered(lambda l: l.user_id.id == each.id)
            sale_order_name = ','.join(filter_sale_order.mapped('name'))
            sheet.write('A%s' % row, serial_number)
            serial_number += 1

            sales_person = {}
            

            for order in filter_sale_order:
                customer_name  = order.user_id.name

                if customer_name not in sales_person:
                    sales_person[customer_name] = {
                        'sale_order_name': [],
                        'invoice_names':[]
                    }
                sales_person[customer_name]['sale_order_name'].append(order.name)
               
                invoices = ''
                amount = 0.0
                amt=[]
                paid = 0.0
                for inv in filter_sale_order.invoice_ids:
                    
                    
                    if inv:
                        invoices += inv.name+','
                        amount = amount+inv.amount_residual
                        paid = paid+(inv.amount_total-inv.amount_residual)
                        # amt.append(paid)

                        
                    

                sheet.write('B%s' % row, customer_name)
                sheet.write('C%s' % row, sale_order_name)
                sheet.write('D%s' % row, invoices)
                sheet.write('E%s' % row, amount)
                # sheet.write('F%s' % row, ', '.join([str(value) for value in amt]))
                sheet.write('F%s' % row, paid)
                
                
                

            

        
            row += 1

         
        

       






       


             


