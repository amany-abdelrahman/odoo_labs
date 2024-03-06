from odoo import models, fields


class Department(models.Model):
    _name = 'department'
    _description = 'Department'

    name = fields.Char()
    capacity = fields.Integer()
    is_opened = fields.Boolean()
    patients = fields.One2many('patient', 'department_id')
    doctors_ids = fields.Many2many('doctor', string='Doctors')
