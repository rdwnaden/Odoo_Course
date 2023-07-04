# -*- coding: utf-8 -*-
# from odoo import http


# class AdhityaAcademy(http.Controller):
#     @http.route('/adhitya_academy/adhitya_academy', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/adhitya_academy/adhitya_academy/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('adhitya_academy.listing', {
#             'root': '/adhitya_academy/adhitya_academy',
#             'objects': http.request.env['adhitya_academy.adhitya_academy'].search([]),
#         })

#     @http.route('/adhitya_academy/adhitya_academy/objects/<model("adhitya_academy.adhitya_academy"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('adhitya_academy.object', {
#             'object': obj
#         })
