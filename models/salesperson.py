# -*- coding: utf-8 -*-

from odoo import models, fields, api

class salesperson(models.Model):
	_inherit = 'res.partner'

	is_salesperson = fields.Boolean(string='Is a Salesperson', default=False)
	# Override field, change default to False
	customer = fields.Boolean(string='Is a Customer', default=False, help="Check this box if this contact is a customer.")