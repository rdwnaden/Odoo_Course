# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class Assign(models.Model):
    _name = 'itsm.assign'
    _inherit = ["mail.thread","mail.activity.mixin"]
    _description = 'Assign'

    name = fields.Char('Form Number', required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'),)
    asset_id = fields.Many2one('itsm.asset', string='Asset Number', Tracking=True)
    category_id = fields.Many2one(string='Category', related='asset_id.category_id', readonly=True)
    old_employee_id = fields.Many2one(string='Used By', related='asset_id.used_id', readonly=True) 
    new_employee_id = fields.Many2one('hr.employee', string='New User', Tracking=True, store=True)
    old_location_id = fields.Many2one(string='Location', related='asset_id.location_id', readonly=True)
    new_location_id = fields.Many2one('itsm.location', string='New Location', Tracking=True, store=True)
    assign_date = fields.Date('Assign Date', Tracking=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('waiting_validate', 'Waiting Validate'),
        ('done', 'Done'),
    ], string='Status', default = 'draft', Tracking=True)
    remarks = fields.Text('Remarks', Tracking=True)

    @api.model
    def create(self, vals):
        seq_date = None
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('itsm.assign') or _('New')
        result = super(Assign, self).create(vals)
        return result

    def action_confirm(self):
        self.state = 'waiting_validate'

    def action_set_draft(self):
        self.state = 'draft'

    def action_done(self):
        self.state = 'done'

    def action_print_assign(self):
        return self.env.ref('itsm.report_itsm_assign_action').report_action(self) 
