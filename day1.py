from math import floor


def get_fuel_requirement(module_weight: int):
    return floor(module_weight / 3) - 2


def get_fuel_requirement_recursive(module_weight: int, running_total: int):
    fuel = get_fuel_requirement(module_weight)
    if fuel < 0:
        return running_total
    return get_fuel_requirement_recursive(fuel, running_total + fuel)


weights = [int(x) for x in open("day1_input.txt", "r").readlines()]
total = 0
total_with_fuel = 0
for weight in weights:
    total += get_fuel_requirement(weight)
    total_with_fuel += get_fuel_requirement_recursive(weight, 0)

print(f"Part 1 - {total}")
print(f"Part 2 - {total_with_fuel}")
