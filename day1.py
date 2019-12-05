from math import floor


def get_fuel_requirement(module_weight: int):
    return floor(module_weight / 3) - 2


def get_fuel_requirement_recursive(module_weight: int, running_total: int):
    fuel = get_fuel_requirement(module_weight)
    if fuel < 0:
        return running_total
    return get_fuel_requirement_recursive(fuel, running_total + fuel)


weights = [int(x) for x in open("day1_input.txt", "r").readlines()]
part_1_total = 0
part_2_total = 0
for weight in weights:
    part_1_total += get_fuel_requirement(weight)
    part_2_total += get_fuel_requirement_recursive(weight, 0)

print(f"Part 1 - {part_1_total}")
print(f"Part 2 - {part_2_total}")

if part_1_total != 3268951 or part_2_total != 4900568:
    raise Exception()
