# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Asset(models.Model):
    _name = 'itsm.asset'
    _inherit = ["mail.thread","mail.activity.mixin"]
    _description = 'Asset'

    name = fields.Char(string='Asset Number', tracking=True)
    picture = fields.Image(string='Picture', tracking=True)
    category_id = fields.Many2one('itsm.category', string='Category', tracking=True)
    serial_number = fields.Char(string='Serial Number', tracking=True)
    purchase_date = fields.Date('Purchase Date', tracking=True)
    company_id = fields.Many2one('res.company', string='Owned By', tracking=True)
    specification = fields.Text('Specification', tracking=True)
    activation_number = fields.Char(string='Activation Number', tracking=True)
    system_model = fields.Char('System Model', tracking=True)
    brand_id = fields.Many2one('itsm.brands', string='Brand', tracking=True)
    services_ids = fields.One2many('itsm.services', 'asset_id', string='Services', readonly=True)
    assign_ids = fields.One2many('itsm.assign', 'asset_id', string='Asset Number', readonly=True)
    credential_ids = fields.One2many('itsm.credential', 'asset_id', string='Credentials', readonly=True)
    used_id = fields.Many2one(string='Used By', related='assign_ids.new_employee_id', readonly=True)
    location_id = fields.Many2one(string='Location', related='assign_ids.new_location_id', readonly=True)
    
    _sql_constraints = [
                     ('name', 
                      'unique(name)',
                      'Asset Number Already Exist!')
    ]
    
