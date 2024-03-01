from odoo import models, fields
class Todo(models.Model):
    _name = 'todo.ticket'
    _description = 'Todo List'
    name = fields.Char(string='Name', required=True)
    number = fields.Char(string='Number')
    tag = fields.Char(string='Tag')
    state = fields.Selection([
        ('new', 'New'),
        ('doing', 'Doing'),
        ('done', 'Done')
    ], string='State', default='new')
    file = fields.Binary(string='File')
    assign_to = fields.Many2one('res.users', string='Assigned To')
    description = fields.Text(string='Description')
