# -*- coding: utf-8 -*-
from odoo import http

# class CmdQuery(http.Controller):
#     @http.route('/cmd_query/cmd_query/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cmd_query/cmd_query/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cmd_query.listing', {
#             'root': '/cmd_query/cmd_query',
#             'objects': http.request.env['cmd_query.cmd_query'].search([]),
#         })

#     @http.route('/cmd_query/cmd_query/objects/<model("cmd_query.cmd_query"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cmd_query.object', {
#             'object': obj
#         })