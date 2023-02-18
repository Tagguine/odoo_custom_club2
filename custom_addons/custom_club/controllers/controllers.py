# -*- coding: utf-8 -*-
# from odoo import http


# class CustomClub(http.Controller):
#     @http.route('/custom_club/custom_club', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_club/custom_club/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_club.listing', {
#             'root': '/custom_club/custom_club',
#             'objects': http.request.env['custom_club.custom_club'].search([]),
#         })

#     @http.route('/custom_club/custom_club/objects/<model("custom_club.custom_club"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_club.object', {
#             'object': obj
#         })
