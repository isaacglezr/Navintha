#-*- coding_ utf-8 -*-
from dateutil.relativedelta import relativedelta
from datetime import timedelta
from openerp import api, fields, models

class emplo_navintha(models.Model):

    _inherit = 'hr.employee'

    x_numempleado = fields.Char(string="Numero de Empleado")
    x_contratacion = fields.Datetime(string="Fecha de Contratacion")
    x_antiguedad = fields.Char(string="Antiguedad", readonly=True, compute='_total_minutes')
    x_observaciones = fields.Text(string="Observaciones")
    x_fechaactual = fields.Datetime(default=fields.Datetime.now)
    x_perfilacademico = fields.Many2one('hr.escolaridad', string="Perfilc Academico")

    @api.one
    @api.depends('x_contratacion','x_fechaactual')
    def _total_minutes(self):
        if self.x_contratacion and self.x_fechaactual:
            start_dt = fields.Datetime.from_string(self.x_contratacion)
            finish_dt = fields.Datetime.from_string(self.x_fechaactual)
            difference = relativedelta(finish_dt, start_dt)
            year = difference.years
            month = difference.months
            days = difference.days
            self.x_antiguedad = str(year)+" anios "+str(month)+" meses "+str(days)+" dias"
        return {}
