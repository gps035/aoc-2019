from math import floor


def get_fuel_requirement(module_weight: int):
    return floor(module_weight / 3) - 2


def get_total_fuel_requirement(module_weight: int):
    def get_fuel_requirement_recursive(weight: int, running_total: int):
        fuel = get_fuel_requirement(weight)
        if fuel < 0:
            return running_total
        return get_fuel_requirement_recursive(fuel, running_total + fuel)

    return get_fuel_requirement_recursive(module_weight, 0)
