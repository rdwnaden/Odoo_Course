# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):
    _name = 'ridwan_academy.course'
    _description = 'ridwan_academy.course'

    name = fields.Char(string='Name')
    user_id = fields.Many2one('res.users', string='Responsible User')
    session_ids = fields.One2many('ridwan_academy.session', 'course_id', string='Session')
    description = fields.Text(string='Description')

