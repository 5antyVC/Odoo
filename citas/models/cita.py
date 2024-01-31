from odoo import models, fields

class Cita(models.Model):
    _name = "citas.cita"
    _description = "Tabla cita"

    Fecha = fields.Date()
   Medico_Asociado = fields.Many2One(citas.medico,string="Medico Asociado")
    Paciente_Asociado = fields.Many2One(citas.paciente,string="Paciente Asociado")
    Estado_Cita = fields.Selection([
        ('disponible', 'Disponible'),
        ('ocupado', 'Ocupado')
    ], string="Estado de la cita")