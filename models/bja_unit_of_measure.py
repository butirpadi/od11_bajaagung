from odoo import models, fields, api

class bja_unit_of_measure(models.Model):
	_name = 'bja.unit_of_measure'

	name = fields.Char('Name', required=True)