from odoo import models, fields, api

class SelectRecordWizard(models.TransientModel):
    _name = 'select.record.wizard'
    _description = 'Wizard to select records and process actions'

    temp_item_ids = fields.Many2many('sms_module.item_selection', string="Items")

    # @api.model
    # def default_get(self, fields):
    #     # self.env['sms_module.item_selection'].search([]).unlink()
    #
    #     res = super(SelectRecordWizard, self).default_get(fields)
    #
    #     # Define the temporary items dynamically
    #     temp_items = [
    #         self.env['sms_module.item_selection'].create({'name': 'Option 1'}).id,
    #         self.env['sms_module.item_selection'].create({'name': 'Option 2'}).id,
    #         self.env['sms_module.item_selection'].create({'name': 'Option 3'}).id,
    #     ]
    #
    #     res.update({'temp_item_ids': [(6, 0, temp_items)]})
    #     return res


    def confirm_action(self):
        # Perform an action based on selected items

        selected_items = self.temp_item_ids
        for item in selected_items:
            # Perform background action based on item.name
            # Example: print each selected item’s name
            print(f"Selected Item: {item}")

        self.temp_item_ids = [(5, 0, 0)]

        # Now safely delete all records in sms_module.item_selection
        self.env['sms_module.item_selection'].search([]).unlink()