from odoo import fields, models


class SaleReport(models.Model):
    _inherit = "sale.report"

    operating_unit_id = fields.Many2one(
        comodel_name="operating.unit",
        string="Operating Unit",
        readonly=True,
    )

    def _select_additional_fields(self):
        result = super()._select_additional_fields()
        result["operating_unit_id"] = "s.operating_unit_id"
        return result

    def _group_by_sale(self):
        return super()._group_by_sale() + ", s.operating_unit_id"