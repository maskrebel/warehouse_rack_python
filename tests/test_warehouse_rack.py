import unittest

from warehouse.warehouse_rack import WarehouseRack


class TestWarehouseRack(unittest.TestCase):
    def setUp(self):
        self.rack = WarehouseRack(6)

    def test_create_rack(self):
        rack = WarehouseRack(3)
        self.assertTrue(True)

    def test_rack(self):
        self.rack.rack("ABC", "2021-01-01")
        self.rack.rack("ADC", "2021-01-01")
        self.rack.rack("BBC", "2022-01-01")
        self.rack.rack("CBC", "2023-01-01")

    def test_rack_out(self):
        pass

    def test_status(self):
        pass

    def sku_numbers_for_product_with_exp_date(self):
        pass

    def slot_numbers_for_product_with_exp_date(self):
        pass

    def slot_number_for_sku_number(self):
        pass
