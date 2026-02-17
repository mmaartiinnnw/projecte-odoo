from odoo import models, fields
class vehiculo(models.Model):
    _name = 'vehiculo'
    _description = 'Vehiculo'

    name = fields.Char(string = 'Matricula' required=True)
    name = fields.Char(string = 'Marca' required=True)
    name = fields.Char(string = 'Modelo' required=True)
    tipo_carnet = fields.Selection([
        ('moto', 'Moto')
        ('coche', 'Coche')
    ],string = 'Tipo de carnet', default='coche')

