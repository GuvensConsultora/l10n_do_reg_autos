# -*- coding: utf-8 -*-
# from odoo import http


# class L10nDoRegAutos/(http.Controller):
#     @http.route('/l10n_do_reg_autos//l10n_do_reg_autos/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/l10n_do_reg_autos//l10n_do_reg_autos//objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('l10n_do_reg_autos/.listing', {
#             'root': '/l10n_do_reg_autos//l10n_do_reg_autos/',
#             'objects': http.request.env['l10n_do_reg_autos/.l10n_do_reg_autos/'].search([]),
#         })

#     @http.route('/l10n_do_reg_autos//l10n_do_reg_autos//objects/<model("l10n_do_reg_autos/.l10n_do_reg_autos/"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('l10n_do_reg_autos/.object', {
#             'object': obj
#         })
