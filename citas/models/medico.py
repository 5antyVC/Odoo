from odoo import models, fields

class Medico(models.Model):
    _name = "citas.medico"
    _description = "Tabla medico"

    

    Nombre = fields.Char(string="Nombre")
    Apellido = fields.Char(string="Apellido")
    Especialidad = fields.Char(string="Especialidad")
    Citas_Asociadas = fields.Char(int="Citas Asociadas")
