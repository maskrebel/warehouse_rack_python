class WarehouseRack:
    def __init__(self, total):
        self.total = total
        self.slots = [None] * self.total
        print(f"Created a warehouse rack with {self.total} slots.")

    def rack(self, sku, expiry_date):
        for idx, slot in enumerate(self.slots):
            if not slot:
                self.slots[idx] = {
                    "sku": sku,
                    "expiry_date": expiry_date
                }
                return f"Allocated slot number: {idx + 1}"

        return "Sorry, rack is full"

    def rack_out(self, slot_number):
        idx = slot_number - 1
        if len(self.slots) >= slot_number:
            self.slots[idx] = None
            return f"Slot number {slot_number} is free"

        else:
            return f"Slot number {slot_number} not found"

    def status(self):
        print("Slot No.\tSKU No.\t\tExp Date")
        for idx, slot in enumerate(self.slots):
            if slot:
                print(f"{idx + 1}\t\t{slot['sku']}\t\t{slot['expiry_date']}")

    def sku_numbers_for_product_with_exp_date(self, exp_date):
        sku = [slot['sku'] for slot in self.slots if slot and slot['expiry_date'] == exp_date]

        msg = "Not found"
        if sku:
            msg = ", ".join(sku)

        return msg

    def slot_numbers_for_product_with_exp_date(self, exp_date):
        slot_numbers = [
            str(idx + 1)
            for idx, slot in enumerate(self.slots)
            if slot and slot['expiry_date'] == exp_date
        ]

        msg = "Not found"
        if slot_numbers:
            msg = ", ".join(slot_numbers)

        return msg

    def slot_number_for_sku_number(self, sku):
        slot_number = "Not found"
        for idx, slot in enumerate(self.slots):
            if slot and slot['sku'] == sku:
                slot_number = idx + 1
                return slot_number

        return slot_number
