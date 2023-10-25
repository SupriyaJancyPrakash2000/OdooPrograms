from odoo import fields, models, api, exceptions
from lxml import etree



class SaleConfirmCheck(models.Model):
    _inherit = 'sale.order'



    def _get_view(self, view_id=None, view_type='form', **options):
        arch, view = super()._get_view(view_id, view_type, **options)

        # Check if the user has manager access
        user = self.env.user
        manager_group = self.env.ref('bi_security_sale.overtime_message_access')

        if view_type == 'tree' and manager_group not in user.groups_id:
            nodes = arch.xpath("//tree")
            for node in nodes:
                node.set('create', '0')  # Hide the "Create" button

        return arch, view


