# -*- coding: utf-8 -*-
# © 2016 Alessandro Fernandes Martini <alessandrofmartini@gmail.com>, Trustcode
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    id_token_csc = fields.Char(string="Identificador do CSC")
    csc = fields.Char(string=u'Código de Segurança do Contribuinte')
