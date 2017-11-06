from odoo import api, fields, models

class ProductTemplate(models.Model):
	_inherit = "product.template"

	bja_uom_id = fields.Many2one('bja.unit_of_measure',string="Unit of Measurement")