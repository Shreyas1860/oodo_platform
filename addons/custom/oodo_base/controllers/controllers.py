# -*- coding: utf-8 -*-
# from odoo import http


# class OodoBase2(http.Controller):
#     @http.route('/oodo_base2/oodo_base2', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/oodo_base2/oodo_base2/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('oodo_base2.listing', {
#             'root': '/oodo_base2/oodo_base2',
#             'objects': http.request.env['oodo_base2.oodo_base2'].search([]),
#         })

#     @http.route('/oodo_base2/oodo_base2/objects/<model("oodo_base2.oodo_base2"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('oodo_base2.object', {
#             'object': obj
#         })

