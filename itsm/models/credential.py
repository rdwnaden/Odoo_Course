# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Credential(models.Model):
    _name = 'itsm.credential'
    _inherit = ["mail.thread","mail.activity.mixin"]
    _description = 'Credential'

    name = fields.Char(string='Device Name', Tracking=True)
    asset_id = fields.Many2one('itsm.asset', string='Asset Number', Tracking=True)
    domain_ip = fields.Char(string='Domain/IP', Tracking=True)
    port = fields.Integer(string='Port', Tracking=True)
    connection_type = fields.Selection([
        ('ssh', 'SSH'),
        ('telnet', 'Telnet'),
        ('ftp', 'FTP'),
        ('web', 'Web'),
        ('winbox', 'Winbox'),
        ('proxy', 'Proxy'),
        ('console', 'Console'),
    ], string='Connection Type', Tracking=True)
    category_id = fields.Many2one('itsm.category', string='Category', Tracking=True)
    username = fields.Char(string='Username', Tracking=True)
    password = fields.Char(string='Password', password=True, Tracking=True)


    _sql_constraints = [
                     ('name', 
                      'unique(name)',
                      'Item Already Exist!')
    ]
    
    