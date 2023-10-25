# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import uuid
from werkzeug.urls import url_encode
from odoo import api, exceptions, fields, models, _


class PortalMixin(models.AbstractModel):
    _inherit = "portal.mixin"

    def get_portal_url_let(self, suffix=None, report_type='pdf', download=True, query_string=None, anchor=None):
        # url = '/my_portal/'+ str(self.id) + '?access_token=%s%s%s%s%s' % (
        #     self._portal_ensure_token(),
        #     '&report_type=%s' % report_type,
        #     '&download=true' if download else '',
        #     query_string if query_string else '',
        #     '#%s' % anchor if anchor else ''
        # )
        url = '/report/pdf/bi_portal_pdf_download.report_task/%s' % self.id
        return url




class ProjectTaskReport(models.AbstractModel):
    _inherit = "project.task"

    def get_rep(self,task):
        return self.env.ref('bi_portal_pdf_download.timesheet_report_task_custom').sudo().report_action(self)





        # task = self.env['project.task'].browse(self.id)
        # self.ensure_one()
        # access_token = self._portal_ensure_token()
        # url = "{}/my/tasks/{}?access_token={}&report_type={}&download={}&{}".format(
        #     self.access_url, self.id, access_token, report_type, download, query_string or '')
        # self.env.ref('bi_portal_pdf_download.timesheet_report_task_custom').report_action(task, data=url)

        # data = {
        #     'start_date': self.start_date,
        #     'end_date': self.end_date,
        #     'journal_name': [rec.code for rec in self.journal_ids],
        #     'account_name': [rec.name for rec in self.accounts_ids],
        #     'target_moves': self.target_moves,
        #     'sort_by': self.sort_by,
        #     'include_initial_balance': self.include_initial_balance,
        #     'accounts_ids': self.accounts_ids.ids,
        #     'journal_ids': self.journal_ids.ids,
        #     'today': self.today
        #
        # }
        # return self.env.ref('bi_portal_pdf_download.portal_pdf_custom').report_action([], data=data)
        #


    # def get_portal_url_let(self):
    #     self.ensure_one()
    #     suffix = '/a'
    #     report_type = 'pdf'
    #     download = True
    #     query_string = None
    #     anchor = 'section-id'
    #
    #     url = self.access_url + '%s?access_token=%s%s%s%s%s' % (
    #         suffix,
    #         self._portal_ensure_token(),
    #         '&report_type=%s' % report_type,
    #         '&download=true' if download else '',
    #         query_string if query_string else '',
    #         '#%s' % anchor if anchor else ''
    #     )
    #     return url