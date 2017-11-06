from odoo import api, fields, models

class KategoriPengeluaran(models.Model):
	_name = "tbr.kategori_pengeluaran"

	name = fields.Char('Name', required=True)
	