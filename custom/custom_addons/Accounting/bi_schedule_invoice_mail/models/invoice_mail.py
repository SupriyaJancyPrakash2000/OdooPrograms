from odoo import models, fields, api, exceptions
from datetime import date
from dateutil.relativedelta import relativedelta
import base64

class InvoiceSend(models.Model):
    _inherit = "account.move"

    payment_remaining_date = fields.Integer(string="Remaining Date")

    def scheduleemail(self):
        invoices = self.env['account.move'].search([('move_type', '=', 'out_invoice'),
                                                    ('payment_state', '=', 'not_paid')])
        current_date = 0
        for each in invoices:
            day = each.payment_remaining_date
            if day != 0:
                current_date = date.today() + relativedelta(days=day)
                all_inv = self.env['account.move'].search([('move_type', '=', 'out_invoice'),
                                                          ('invoice_date_due', '=', current_date),
                                                          ('payment_state', '=', 'not_paid')])

                email_template = self.env.ref('bi_schedule_invoice_mail.email_template_edi_invoice_123')
                for each_inv in all_inv:
                    invoice_report = self.env.ref('account.account_invoices')
                    data_record = base64.b64encode(
                        self.env['ir.actions.report'].sudo()._render_qweb_pdf(
                            invoice_report, [each_inv.id], data=None)[0])

                    dte_attachment = self.env['ir.attachment'].create({
                        'name': 'Invoice Report.pdf',
                        'res_model': each_inv._name,
                        'res_id': each_inv.id,
                        'type': 'binary',
                        'datas': data_record,
                    })

                    try:
                        email_template.send_mail(
                            each_inv.id,
                            force_send=True,
                            email_values={'attachment_ids': [(6, 0, [dte_attachment.id])]}
                        )

                    except exceptions.UserError as e:
                        pass




