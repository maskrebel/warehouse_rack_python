import unittest

from warehouse.rack.service import WarehouseRack


class TestWarehouseRack(unittest.TestCase):
    def setUp(self):
        self.rack = WarehouseRack(4)
        self.sample_date = "2021-01-01"
        self.sample_sku = "ABC"
        self.sample_date_failed = "2024-02-01"
        self.sample_sku_failed = "DAD"

        self.rack.rack("ABC", "2021-01-01")
        self.rack.rack("ADC", "2021-01-01")
        self.rack.rack("BBC", "2022-01-01")

    def test_create_rack(self):
        total = 3
        rack = WarehouseRack(total)
        self.assertEquals(rack.total, total)

    def test_rack(self):
        res = self.rack.rack("DBC", "2024-01-01")

        self.assertEquals(sum(1 for slot in self.rack.slots if slot), 4)
        self.assertEquals(res, 'Allocated slot number: 4')

        res_is_full = self.rack.rack("DDC", "2024-01-01")
        self.assertEquals(res_is_full, 'Sorry, rack is full')

    def test_rack_out(self):
        self.rack.rack_out(1)
        self.assertEquals(sum(1 for slot in self.rack.slots if slot), 2)

    def test_status(self):
        self.rack.status()
        self.assertEquals(sum(1 for slot in self.rack.slots if slot), 3)

    def test_sku_numbers_for_product_with_exp_date(self):
        res = self.rack.sku_numbers_for_product_with_exp_date(self.sample_date)
        res_failed = self.rack.sku_numbers_for_product_with_exp_date(self.sample_date_failed)

        self.assertEquals(res, 'ABC, ADC')
        self.assertEquals(res_failed, 'Not found')

    def test_slot_numbers_for_product_with_exp_date(self):
        res = self.rack.slot_numbers_for_product_with_exp_date(self.sample_date)
        res_failed = self.rack.slot_numbers_for_product_with_exp_date(self.sample_date_failed)

        self.assertEquals(res, '1, 2')
        self.assertEquals(res_failed, 'Not found')

    def test_slot_number_for_sku_number(self):
        res = self.rack.slot_number_for_sku_number(self.sample_sku)
        res_failed = self.rack.slot_number_for_sku_number(self.sample_sku_failed)

        self.assertEquals(res, 1)
        self.assertEquals(res_failed, 'Not found')
