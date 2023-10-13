# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Renewal(models.Model):
    _name = 'itsm.renewal'
    _inherit = ["mail.thread","mail.activity.mixin"]
    _description = 'Renewal and Subscribtion'

    name = fields.Char(string='Item Name', Tracking=True)
    vendor_id = fields.Many2one('res.partner', string='Vendor', Tracking=True)
    register_date = fields.Date(string='Register Date', Tracking=True)
    item_category = fields.Selection([
        ('domain', 'Domain'),
        ('internet', 'Internet'),
        ('telephone', 'Telephone'),
        ('email', 'Email'),
        ('system', 'System'),
        ('license', 'License'),
        ('antivirus', 'Antivirus'),
    ], string='Item Category', Tracking=True)
    period = fields.Selection([
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly'),
    ], string='Payment Period', Tracking=True)
    remarks = fields.Text(string='Remarks')
    

    _sql_constraints = [
                     ('name', 
                      'unique(name)',
                      'Item Name Already Exist!')
    ]
    