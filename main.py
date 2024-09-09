import sys


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
                print(f"Allocated slot number: {idx + 1}")
                return

        print("Sorry, rack is full")

    def rack_out(self, slot_number):
        idx = slot_number - 1
        if len(self.slots) >= slot_number:
            self.slots[idx] = None
            print(f"Slot number {slot_number} is free")

        else:
            print(f"Slot number {slot_number} not found")

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

        print(msg)

    def slot_numbers_for_product_with_exp_date(self, exp_date):
        slot_numbers = [
            str(idx + 1)
            for idx, slot in enumerate(self.slots)
            if slot and slot['expiry_date'] == exp_date
        ]

        res = "Not found"
        if slot_numbers:
            res = ", ".join(slot_numbers)

        print(res)

    def slot_number_for_sku_number(self, sku):
        slot_number = "Not found"
        for idx, slot in enumerate(self.slots):
            if slot and slot['sku'] == sku:
                slot_number = idx + 1
                print(slot_number)
                return

        print(slot_number)


class Validator:
    def __init__(self, commands):
        self.commands = commands
        self.action = commands[0]
        self.map_action_validation = {
            "create_warehouse_rack": {
                "count": 2,
                "fields": (commands[1].isdigit(), True) if len(commands) >= 2 else (False, True)
            },
            "create_rack": {
                "count": 2,
                "fields": (commands[1].isdigit(), True) if len(commands) >= 2 else (False, True)
            },
            "rack": {
                "count": 3,
                "fields": self.validate_date(commands[2]) if self.action == "rack" else False
            },
            "rack_out": {
                "count": 2,
            },
            "status": {
                "count": 1,
            },
            "sku_numbers_for_product_with_exp_date": {
                "count": 2,
                "fields": self.validate_date(commands[1])
                if self.action == "sku_numbers_for_product_with_exp_date" else False,
            },
            "slot_numbers_for_product_with_exp_date": {
                "count": 2,
                "fields": self.validate_date(commands[1])
                if self.action == "slot_numbers_for_product_with_exp_date" else False,
            },
            "slot_number_for_sku_number": {
                "count": 2,
            }
        }

    def validate_date(self, exp_date):
        res = [True, True]

        date_split = exp_date.split("-")
        if not len(date_split) == 3:
            res = [False, True]

        else:
            year, month, day = date_split
            if len(year) != 4 or len(month) != 2 or len(day) != 2:
                res = [False, True]

            elif not year.isdigit() or not month.isdigit() or not day.isdigit():
                res = [False, True]

        return res

    def valid(self):
        result = self.map_action_validation[self.action]

        res = None
        if not len(self.commands) == result["count"]:
            res = f"{self.action} need {result['count']} arguments"

        elif result.get("fields"):
            need, expected = result["fields"]
            if need != expected:
                res = f"{self.action} fields is missing"

        return res

def preprocessing(commands, rack):
    action = commands[0]
    if not action:
        return

    if action in ['create_rack', 'create_warehouse_rack']:
        validation = Validator(commands)
        if failure:= validation.valid():
            print(failure)
            return

        else:
            total = int(commands[1])
            return WarehouseRack(total)

    if not rack:
        print("Please create a rack first using 'create_rack'.")

    elif action == 'rack':
        validation = Validator(commands)
        if failure := validation.valid():
            print(failure)

        else:
            sku = commands[1]
            expiry_date = commands[2]
            rack.rack(sku, expiry_date)

    elif action == 'rack_out':
        validation = Validator(commands)
        if failure := validation.valid():
            print(failure)

        else:
            slot_number = int(commands[1])
            rack.rack_out(slot_number)

    elif action == 'status':
        validation = Validator(commands)
        if failure := validation.valid():
            print(failure)

        else:
            rack.status()

    elif action == 'sku_numbers_for_product_with_exp_date':
        validation = Validator(commands)
        if failure := validation.valid():
            print(failure)

        else:
            exp_date = commands[1]
            rack.sku_numbers_for_product_with_exp_date(exp_date)

    elif action == 'slot_numbers_for_product_with_exp_date':
        validation = Validator(commands)
        if failure := validation.valid():
            print(failure)

        else:
            exp_date = commands[1]
            rack.slot_numbers_for_product_with_exp_date(exp_date)

    elif action == 'slot_number_for_sku_number':
        validation = Validator(commands)
        if failure := validation.valid():
            print(failure)

        else:
            sku = commands[1]
            rack.slot_number_for_sku_number(sku)

    else:
        print("Unknown command.")

    return rack


def main():
    rack = None
    if len(sys.argv) == 1:
        while True:
            commands = input().split()
            if commands[0] == "exit":
                break

            rack = preprocessing(commands, rack)

    else:
        try:
            with open(sys.argv[1], "r") as file:
                for line in file:
                    line = line.strip().split()
                    rack = preprocessing(line, rack)
        except FileNotFoundError:
            print("File not found")



if __name__ == '__main__':
    print("start")
    main()
