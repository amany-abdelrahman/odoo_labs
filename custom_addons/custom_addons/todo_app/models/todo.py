from odoo import models, fields


class Todo(models.Model):
    _name = 'todo.ticket'
    _description = 'Todo List'
    name = fields.Char()
    number = fields.Char()
    tag = fields.Char()
    state = fields.Selection([
        ('new', 'New'),
        ('doing', 'Doing'),
        ('done', 'Done')
    ])
    file = fields.Binary()
    assign_to = fields.Many2one('res.users')
    description = fields.Text()
