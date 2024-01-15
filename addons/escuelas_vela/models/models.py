# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Escuela(models.Model):
    _name = 'escuelas_vela.escuela'
    _description = 'Escuela de Vela'

    name = fields.Char(string='Denominación')
    logo = fields.Binary(string='Logotipo')
    telefono = fields.Char(string='Teléfono')
    direccion = fields.Text(string='Dirección')
    ciudad = fields.Char(string='Ciudad')
    codigo_postal = fields.Char(string='Código Postal')
    cursos_ids = fields.One2many('escuelas_vela.curso', 'escuela_id', string='Cursos')

class Curso(models.Model):
    _name = 'escuelas_vela.curso'
    _description = 'Curso de Vela'

    title = fields.Char(string='Título')
    duration_days = fields.Integer(string='Duración en Días')
    duration_hours = fields.Integer(string='Duración en Horas')
    price = fields.Float(string='Precio')
    escuela_id = fields.Many2one('escuelas_vela.escuela', string='Escuela')
    monitores_ids = fields.Many2many('escuelas_vela.monitor', string='Monitores')

class Monitor(models.Model):
    _name = 'escuelas_vela.monitor'
    _description = 'Monitor de Vela'

    name = fields.Char(string='Nombre')
    telefono = fields.Char(string='Teléfono')
    direccion = fields.Text(string='Dirección')
    ciudad = fields.Char(string='Ciudad')
    codigo_postal = fields.Char(string='Código Postal')
    identification_code = fields.Char(string='Código de Identificación', required=True)
    escuelas_ids = fields.Many2many('escuelas_vela.escuela', string='Escuelas')

class Alumno(models.Model):
    _name = 'escuelas_vela.alumno'
    _description = 'Alumno de Vela'

    name = fields.Char(string='Nombre')
    telefono = fields.Char(string='Teléfono')
    direccion = fields.Text(string='Dirección')
    ciudad = fields.Char(string='Ciudad')
    codigo_postal = fields.Char(string='Código Postal')
    enrollment_number = fields.Char(string='Número de Matrícula', required=True)
    escuela_id = fields.Many2one('escuelas_vela.escuela', string='Escuela')