from odoo import api, fields, models

class Pengeluaran(models.Model):
	_name = "tbr.pengeluaran"

	name = fields.Char('Name', required=True)
	kategori_id = fields.Many2one('tbr.kategori_pengeluaran', string="Kategori")
	tanggal = fields.Date('Date', required=True)
	amount = fields.Float('Amount',required=True, default=0.0)
	