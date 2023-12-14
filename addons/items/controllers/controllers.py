# -*- coding: utf-8 -*-
# from odoo import http


# class Items(http.Controller):
#     @http.route('/items/items', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/items/items/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('items.listing', {
#             'root': '/items/items',
#             'objects': http.request.env['items.items'].search([]),
#         })

#     @http.route('/items/items/objects/<model("items.items"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('items.object', {
#             'object': obj
#         })

