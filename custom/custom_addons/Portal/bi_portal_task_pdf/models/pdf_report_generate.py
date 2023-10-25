from odoo import fields,models

class ReportPdf(models.AbstractModel):
    _inherit = "portal.mixin"

    #
    # def get_pdf_portal_url(self):
    #     pass
    # suffix = None, report_type = None, download = None, query_string = None, anchor = None
    def get_task_pdf_portal_url(self, suffix=None, report_type='pdf', download=True, query_string=None, anchor=None):
        print(">>>>>>>>>>>>>>>>")

        url = '/report/pdf/bi_portal_task_pdf.action_task_pdf_report_download/%s' % self.id
        return url
