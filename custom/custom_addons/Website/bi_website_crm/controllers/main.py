from odoo import http
from odoo.http import request


class CrmWebsite(http.Controller):

    @http.route('/service', type='http', auth='public', website=True)
    def custom_website_page(self):
        events = request.env['product.info'].search([('is_published', '=', True)])
        return request.render('bi_website_crm.new_page', {'events': events})

    @http.route('/service/Enquiry', type='http', auth='public', website=True)
    def custom_website_page_enquiry(self):
        return request.render('bi_website_crm.new_form_template', {'events': "list"})

    @http.route('/enquiry-form/submit', type='http', auth='public', website=True, csrf=False)
    def submit_enquiry_form(self, **post):
        # Create a CRM lead with the submitted data
        Lead = request.env['crm.lead']
        lead_data = {
            'name': post.get('name'),
            # 'partner_id': post.get('company'),
            'phone': post.get('phone'),
            'email_from': post.get('email'),

        }
        new_lead = Lead.create(lead_data)
        return request.render('bi_website_crm.contacts')