from odoo import models, fields


class LogHistory(models.Model):
    _name = 'log.history'
    _description = 'Log History for Patients'

    created_by = fields.char()
    date = fields.Datetime(default=fields.Datetime.now)
    description = fields.Text()
    patient_id = fields.Many2one('patient')
