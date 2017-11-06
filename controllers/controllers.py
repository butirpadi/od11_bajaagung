# -*- coding: utf-8 -*-
from odoo import http

# class BjaApp(http.Controller):
#     @http.route('/bja_app/bja_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bja_app/bja_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bja_app.listing', {
#             'root': '/bja_app/bja_app',
#             'objects': http.request.env['bja_app.bja_app'].search([]),
#         })

#     @http.route('/bja_app/bja_app/objects/<model("bja_app.bja_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bja_app.object', {
#             'object': obj
#         })