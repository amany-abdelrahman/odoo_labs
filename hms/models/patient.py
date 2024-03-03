from odoo import models, fields, api
from odoo.exceptions import ValidationError
from dateutil.relativedelta import relativedelta

class PatientLog(models.Model):
    _name = 'patient.log'
    _description = 'Patient Log'

    patient_id = fields.Many2one('patient')
    created_by = fields.Many2one('res.users', default=lambda self: self.env.user)
    date = fields.Datetime(default=fields.Datetime.now)
    description = fields.Text()

class Patient(models.Model):
    _name = 'patient'
    _description = 'Patient'
    first_name = fields.Char()
    last_name = fields.Char()
    birth_date = fields.Date()
    history = fields.Html()
    cr_ratio = fields.Float()
    blood_type = fields.Selection([
        ('A', 'A'),
        ('B', 'B'),
        ('O', 'O'),
        ('AB', 'AB'),
    ])
    pcr = fields.Boolean()
    image = fields.Binary()
    address = fields.Text()
    age = fields.Integer(compute='_compute_age', store=True)
    department_id = fields.Many2one('department')
    doctors_ids = fields.Many2many('doctor')
    state = fields.Selection([
        ('undetermined', 'Undetermined'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('serious', 'Serious'),
    ])
    log_ids = fields.One2many('patient.log', 'patient_id')


@api.depends('birth_date')
def _compute_age(self):
    for rec in self:
        if rec.birth_date:
            birth_date = fields.Date.from_string(rec.birth_date)
            rec.age = relativedelta(fields.Date.today(), birth_date).years
        else:
            rec.age = False


@api.depends('age')
def _compute_history(self):
    for rec in self:
        if rec.age < 50:
            rec.history = False
        else:
            rec.history = rec._compute_history_log()

@api.depends('state')
def _compute_history_log(self):
    for rec in self:
        if rec.state == 'undetermined':
            rec.history_log = 'State is undetermined.'
        elif rec.state == 'good':
            rec.history_log = 'State is good.'
        elif rec.state == 'fair':
            rec.history_log = 'State is fair.'
        elif rec.state == 'serious':
            rec.history_log = 'State is serious.'

@api.onchange('age')
def _onchange_pcr(self):
    if self.age < 30:
        self.pcr = True
        raise ValidationError('PCR is automatically checked')


@api.onchange('state')
def _onchange_state(self):
    self._create_log_record()


def _create_log_record(self):
    log_description = f'State changed to {self.state.upper()}'
    self.env['patient.log'].create({
        'patient_id': self.id,
        'created_by': self.env.user.id,
        'description': log_description
    })


@api.constrains('department_id')
def _check_dept_is_opened(self):
    for rec in self:
        if rec.department_id and not rec.department_id.is_opened:
            raise ValidationError('This department is close, Please select an open department.')


@api.onchange('department_id')
def _onchange_dept_id(self):
    for rec in self:
        if rec.department_id:
            rec.doctors_ids = [(6, 0, rec.department_id.doctors_ids.ids)]


@api.onchange('pcr')
def _onchange_pcr(self):
    for rec in self:
        if rec.pcr and not rec.cr_ratio:
            raise ValidationError('Please provide CR Ratio when PCR is selected.')


@api.onchange('age')
def _onchange_age(self):
    for rec in self:
        if rec.age < 50:
            rec.history = False
        else:
            rec.history = rec._compute_history_log()
        if rec.age < 30:
            rec.pcr = True
            raise ValidationError('PCR is automatically enabled for patients under 30 years of age.')
