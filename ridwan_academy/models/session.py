# -*- coding: utf-8 -*-

from email.policy import default
from odoo import models, fields, api

class Session(models.Model):
    _name = 'ridwan_academy.session'
    _description = 'ridwan_academy.session'

    name = fields.Char(string='Name')
    partner_id = fields.Many2one('res.partner', string='Instructor')
    course_id = fields.Many2one('ridwan_academy.course', string='Course')
    partner_ids = fields.Many2many('res.partner', string='Attendees')
    start_date = fields.Datetime('Start Date')
    duration = fields.Float('Duration')
    number_of_seats = fields.Float('Number of Seats')
    taken_seats = fields.Float('Taken Seats', compute='_count_taken_seats')
    active = fields.Boolean(default = True)

    @api.depends('number_of_seats','partner_ids')
    def _count_taken_seats(self):
        for rec in self:
            if rec.number_of_seats and len(rec.partner_ids):
                rec.taken_seats = len(rec.partner_ids) / rec.number_of_seats * 100
            else:
                rec.taken_seats = 0