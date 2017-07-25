from openerp import fields, models, api

class EmployeeN(models.Model):

    _name = 'employee.navintha'

    x_numempleado = fields.Char(string="Numero de Empleado")
    x_contratacion = fields.Date(string="Fecha de Contratacion")
    x_antiguedad = fields.Integer(string="Antiguedad", readonly=True)
    x_perfilacademico = fields.Many2one('hr.escolaridad', string="Perfil Academico")



