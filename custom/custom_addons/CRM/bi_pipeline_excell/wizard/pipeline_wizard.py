from odoo import models,fields,api


class PipelineWizard(models.TransientModel):
    _name = 'pipeline.wizard'

    date_from = fields.Date('Date from')
    date_to = fields.Date('Date to')
    sale_per = fields.Many2one('res.users', string="Sales Person")

    def action_generate(self):
        data = {
            'ids': self.ids,
            'model': self._name,
            'form': {'date_from': self.date_from,
                     'date_to': self.date_to,
                     'sale_per': self.sale_per.id

                     }

        }
        return self.env.ref('bi_pipeline_excell.action_openacademy_crmpipelinexlsx_report').report_action(self, data=data)