# -*- coding: utf-8 -*-
# from odoo import http


# class AiSimpleLibrary(http.Controller):
#     @http.route('/ai_simple_library/ai_simple_library/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ai_simple_library/ai_simple_library/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ai_simple_library.listing', {
#             'root': '/ai_simple_library/ai_simple_library',
#             'objects': http.request.env['ai_simple_library.ai_simple_library'].search([]),
#         })

#     @http.route('/ai_simple_library/ai_simple_library/objects/<model("ai_simple_library.ai_simple_library"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ai_simple_library.object', {
#             'object': obj
#         })
