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
