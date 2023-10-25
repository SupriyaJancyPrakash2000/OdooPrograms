from odoo import fields, models,api


class NameSearch(models.Model):
    _inherit = 'res.partner'


    cus_code = fields.Char(string="Customer code")

    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None):
        args = list(args or [])
        if name:
            args += ['|', '|', ('name', operator, name), ('email', operator, name),
                     ('cus_code', operator, name)]
        return self._search(args, limit=limit, access_rights_uid=name_get_uid)