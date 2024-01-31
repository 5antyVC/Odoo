from odoo import models, fields

class Paciente(models.Model):
    _name = "citas.paciente"
    _description = "Tabla paciente"

    

    Nombre = fields.Char(string="Nombre")
    Apellido = fields.Char(string="Apellido")
    Género = fields.Selection([
        ('maculino', 'femenino'),
    ], string="Género")
    Citas_Solicitadas = fields.Integer(string="Citas Solicitadas")
