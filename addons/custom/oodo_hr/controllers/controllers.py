# -*- coding: utf-8 -*-
# from odoo import http


# class OodoHr(http.Controller):
#     @http.route('/oodo_hr/oodo_hr', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/oodo_hr/oodo_hr/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('oodo_hr.listing', {
#             'root': '/oodo_hr/oodo_hr',
#             'objects': http.request.env['oodo_hr.oodo_hr'].search([]),
#         })

#     @http.route('/oodo_hr/oodo_hr/objects/<model("oodo_hr.oodo_hr"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('oodo_hr.object', {
#             'object': obj
#         })

