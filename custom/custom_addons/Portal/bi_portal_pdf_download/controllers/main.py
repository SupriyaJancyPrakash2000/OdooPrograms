from odoo import http
from odoo.http import request
from odoo.osv.expression import AND, OR
from odoo.exceptions import MissingError, ValidationError, AccessError
from odoo.addons.documents.controllers.main import ShareRoute

class DocumentsForWebPortal(ShareRoute):

    # @http.route('/my_portal/', type='http', auth="user", website=True, methods=['GET'])
    # def _show_task_report_custom(self, task_sudo=None, report_type='pdf', download=True):
    #     task = request.env['project.task'].browse(request.params['task_id'])
    #
    #     response = request.env.ref('bi_portal_pdf_download.timesheet_report_task_custom').sudo().report_action(docids=task)
    #     return response
        #
        @http.route('/my_portal/<int:task_id>', type='http', auth="public")
        def _show_task_report_custom(self, task_sudo=None, report_type='pdf', download=True):
            task = request.env['project.task'].browse(request.params['task_id'])
            # task.get_rep(task)
            # response = request.ref('bi_portal_pdf_download.timesheet_report_task_custom').sudo().report_action(task)
            try:
                documents = self._check_access_and_get_shared_documents(task.id, access_token=request.params['access_token'])
            except (AccessError, MissingError):
                return request.redirect('/my')

            if not documents:
                raise request.not_found()

            task_name = task.name
            return self._make_zip(task_name + '.zip', documents)

        # @http.route('/my_portal/<int:task_id>', type='http', auth="user", website=True, methods=['GET'])
        # def _show_task_report_custom(self, task_sudo=None, report_type='pdf', download=True):
        #     task = request.env['project.task'].browse(request.params['task_id'])
        #
        #     context = {
        #         'lang': 'en_US',
        #         'tz': 'Asia/Kolkata',
        #         'uid': request.env.user.id,
        #         'allowed_company_ids': [1],
        #         'website_id': request.website.id,
        #         'edit_translations': False,
        #         'active_ids': [task.id],
        #     }
        #
        #     response = request.env.ref('bi_portal_pdf_download.timesheet_report_task_custom').sudo().report_action(
        #         docids=task.ids,  # Pass a list of docids
        #         data={
        #             'context': context
        #         }
        #     )
        #
        #     return response



        # domain = request.env['account.analytic.line']._timesheet_get_portal_domain()
        # task_domain = AND([domain, [('task_id', '=', task_sudo.id)]])
        # timesheets = request.env['account.analytic.line'].sudo().search(task_domain)
        # return self._show_report(model=timesheets,
        #                          report_type=report_type, report_ref='hr_timesheet.timesheet_report_task_timesheets',
        #                          download=download)






    # def customer_portal_url(self):
    #     # Render the custom template
    #     response = http.request.render('bi_portal_pdf_download.timesheet_report_task_custom')

        # Set the content type to PDF
        # response.headers['Content-Type'] = 'application/pdf'
        #
        # # Set the Content-Disposition header to force download
        # response.headers['Content-Disposition'] = "attachment; filename=portal_pdf_custom.pdf"

        # return response

