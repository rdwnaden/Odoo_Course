# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Dashboard(models.Model):
    _name = 'itsm.dashboard'
    _inherit = ["board.board"]
    _description = 'Dashboard'

    name = fields.Char(string='Name')
    
    