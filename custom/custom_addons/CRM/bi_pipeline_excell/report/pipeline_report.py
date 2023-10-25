from odoo import models, fields, api


class Excell_report(models.AbstractModel):
    _name = 'report.bi_pipeline_excell.openacademy_inventoryxlsx_report'
    _inherit = "report.report_xlsx.abstract"

    def generate_xlsx_report(self, workbook, data, lines):
        sheet = workbook.add_worksheet("sale order report")
        bold = workbook.add_format({'bold': True, 'align': 'center', })
        title = workbook.add_format({'bold' : True, 'align': 'center', 'font_size': 10, 'border': True})

        date_from = data['form']['date_from']
        date_to = data['form']['date_to']
        sale_per = data['form']['sale_per']
        domain = [('stage_id.is_won', '=', True)]

        if date_from:
            domain.append(('create_date', '>=', date_from))
        if date_to:
            domain.append(('create_date', '<=', date_to))

        if sale_per:
            domain.append(('user_id', '=', sale_per))

        crm_lead = self.env['crm.lead'].search(domain)

        if crm_lead:
            row = 3
            serial_number = 1
            sheet.merge_range('A1:G1', 'CRM Lead Won', title)
            sheet.write('A2', 'Sl.No', bold)
            sheet.write('B2', 'Name', bold)
            sheet.write('C2', 'Date', bold)
            sheet.write('D2', 'Customer', bold)
            sheet.write('E2', 'Probability', bold)
            sheet.write('F2', 'Expected Revenue', bold)
            sheet.write('G2', 'Sale_Person', bold)

            amount_total = 0

            for order in crm_lead:
                order_date = order.create_date
                date_d = order_date.strftime('%Y-%m-%d')

                sheet.write('A%s' % row, serial_number)
                serial_number += 1
                sheet.set_column('A:A', 8)
                sheet.write('B%s' % row, order.name)
                sheet.set_column('B:B', 15)
                sheet.write('C%s' % row, date_d)
                sheet.set_column('C:C', 15)
                sheet.write('D%s' % row, order.partner_id.name)
                sheet.set_column('D:D', 15)
                sheet.write('E%s' % row, order.probability)
                sheet.set_column('E:E', 15)
                sheet.write('F%s' % row, order.expected_revenue)
                sheet.set_column('F:F', 15)
                sheet.write('G%s' % row, order.user_id.name)
                sheet.set_column('G:G', 15)
                row += 1
                amount_total += order.expected_revenue

            row += 1
            sheet.write('F%s' % row, "Total", bold)
            sheet.write('G%s' % row, amount_total)
        else:
            print("No report found")