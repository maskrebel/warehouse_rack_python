import sys

from warehouse.rack.validator import ValidatorWarehouseRack
from warehouse.rack.service import WarehouseRack


def preprocessing(commands, rack):
    action = commands[0]
    if not action:
        return

    if action in ['create_rack', 'create_warehouse_rack']:
        validation = ValidatorWarehouseRack(commands)
        if failure := validation.valid():
            print(failure)
            return

        else:
            total = int(commands[1])
            return WarehouseRack(total)

    if not rack:
        print("Please create a rack first using 'create_rack'.")

    elif action == 'rack':
        validation = ValidatorWarehouseRack(commands)
        if failure := validation.valid():
            print(failure)

        else:
            sku = commands[1]
            expiry_date = commands[2]
            res = rack.rack(sku, expiry_date)
            print(res)

    elif action == 'rack_out':
        validation = ValidatorWarehouseRack(commands)
        if failure := validation.valid():
            print(failure)

        else:
            slot_number = int(commands[1])
            res = rack.rack_out(slot_number)
            print(res)

    elif action == 'status':
        validation = ValidatorWarehouseRack(commands)
        if failure := validation.valid():
            print(failure)

        else:
            rack.status()

    elif action == 'sku_numbers_for_product_with_exp_date':
        validation = ValidatorWarehouseRack(commands)
        if failure := validation.valid():
            print(failure)

        else:
            exp_date = commands[1]
            res = rack.sku_numbers_for_product_with_exp_date(exp_date)
            print(res)

    elif action == 'slot_numbers_for_product_with_exp_date':
        validation = ValidatorWarehouseRack(commands)
        if failure := validation.valid():
            print(failure)

        else:
            exp_date = commands[1]
            res = rack.slot_numbers_for_product_with_exp_date(exp_date)
            print(res)

    elif action == 'slot_number_for_sku_number':
        validation = ValidatorWarehouseRack(commands)
        if failure := validation.valid():
            print(failure)

        else:
            sku = commands[1]
            res = rack.slot_number_for_sku_number(sku)
            print(res)

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
