import itertools
from typing import List, Tuple

import solution_inputs
from amplifiers import run_amps, NUMBER_OF_AMPS
from fuel import get_fuel_requirement, get_total_fuel_requirement
from image_decoding import calculate_checksum, flatten_layers
from intcode_computer import run_program
from orbits import orbital_transfers_required, count_total_orbits
from passwords import is_valid_password_simple, is_valid_password_strict
from wires import calculate_closest_intersection_to_origin, calculate_closest_intersection_along_wires

print("\nDay 1")

day1_part1_result = sum([get_fuel_requirement(weight) for weight in solution_inputs.day1_input])
day1_part2_result = sum([get_total_fuel_requirement(weight) for weight in solution_inputs.day1_input])

print(f"Part 1 - {day1_part1_result}")
print(f"Part 2 - {day1_part2_result}")

if day1_part1_result != 3268951 or day1_part2_result != 4900568:
    raise Exception()

print("\nDay 2")


def run_program_with_noun_and_verb(program: List[int], noun: int, verb: int):
    program_copy = program.copy()
    program_copy[1] = noun
    program_copy[2] = verb
    for _ in run_program(program_copy):
        pass
    return program_copy[0]


def find_noun_and_verb(expected_result: int, program: List[int]):
    for n in range(0, 99):
        for v in range(0, 99):
            this_output = run_program_with_noun_and_verb(program, n, v)
            if this_output == expected_result:
                return (n * 100) + v


day2_part1_result = run_program_with_noun_and_verb(solution_inputs.day2_input, 12, 2)
day2_part2_result = find_noun_and_verb(19690720, solution_inputs.day2_input)

print(f"Part 1: {day2_part1_result}")
print(f"Part 2: {day2_part2_result}")

if day2_part1_result != 2890696 or day2_part2_result != 8226:
    raise Exception()

print("\nDay 3")

day3_part1_result = calculate_closest_intersection_to_origin(solution_inputs.day3_input)
day3_part2_result = calculate_closest_intersection_along_wires(solution_inputs.day3_input)

print(f"Part 1: {day3_part1_result}")
print(f"Part 2: {day3_part2_result}")

if day3_part1_result != 865 or day3_part2_result != 35038:
    raise Exception()

print("\nDay 4")

min_value = solution_inputs.day4_input[0]
max_value = solution_inputs.day4_input[1]

day4_part1_result = sum([1 for x in range(min_value, max_value + 1) if is_valid_password_simple(str(x))])
day4_part2_result = sum([1 for x in range(min_value, max_value + 1) if is_valid_password_strict(str(x))])

print(f"Part 1: {day4_part1_result}")
print(f"Part 2: {day4_part2_result}")

if day4_part1_result != 1650 or day4_part2_result != 1129:
    raise Exception()

print("\nDay 5")


def get_last_output(program: List[int], program_input: List[int] = None):
    last_output = 0
    for last_output in run_program(program, program_input):
        pass
    return last_output


# air_con_diagnostic_code
day5_part1_result = get_last_output(solution_inputs.day5_input.copy(), [1])

# thermal_radiator_diagnostic_code
day5_part2_result = get_last_output(solution_inputs.day5_input.copy(), [5])

print(f"Part 1: {day5_part1_result}")
print(f"Part 2: {day5_part2_result}")

if day5_part1_result != 15508323 or day5_part2_result != 9006327:
    raise Exception()

print("\nDay 6")

day6_part1_result = count_total_orbits(solution_inputs.day6_input)
day6_part2_result = orbital_transfers_required(solution_inputs.day6_input, "YOU", "SAN")

print(f"Part 1: {day6_part1_result}")
print(f"Part 2: {day6_part2_result}")

if day6_part1_result != 249308 or day6_part2_result != 349:
    raise Exception()

print("\nDay 7")


def calculate_best_output_for_phase_setting_permutations(
        program: List[int],
        possible_phase_settings: Tuple[int, int, int, int, int]
):
    best_output = 0
    for phase_settings in list(itertools.permutations(possible_phase_settings, NUMBER_OF_AMPS)):
        output = run_amps(program, phase_settings)
        if output > best_output:
            best_output = output
    return best_output


day7_part1_result = calculate_best_output_for_phase_setting_permutations(solution_inputs.day7_input.copy(),
                                                                         (0, 1, 2, 3, 4))
day7_part2_result = calculate_best_output_for_phase_setting_permutations(solution_inputs.day7_input.copy(),
                                                                         (5, 6, 7, 8, 9))

print(f"Part 1: {day7_part1_result}")
print(f"Part 2: {day7_part2_result}")

if day7_part1_result != 116680 or day7_part2_result != 89603079:
    raise Exception()

print("\nDay 8")

width = 25
height = 6
day8_part1_result = calculate_checksum(solution_inputs.day8_input, width, height)
day8_part2_result = flatten_layers(solution_inputs.day8_input, width, height)


def render_image(image: str, image_width: int):
    first_index = 0
    while first_index < len(image):
        row = image[first_index:first_index + image_width]
        first_index += image_width
        print(row.replace("0", "░░").replace("1", "██"))


print(f"Part 1: {day8_part1_result}")
print(f"Part 2:")
render_image(day8_part2_result, width)

if day8_part1_result != 1596 or day8_part2_result != "100001110011100011001111010000100101001010010100001000011100100101000011100100001001011100100001000010000100101010010010100001111011100100100110011110":
    raise Exception()

print("\nDay 9")

day9_part1_result = list(run_program(solution_inputs.day9_input.copy(), [1]))
day9_part2_result = list(run_program(solution_inputs.day9_input.copy(), [2]))


print(f"Part 1: {day9_part1_result}")
print(f"Part 2: {day9_part2_result}")

if day9_part1_result != [2453265701] or day9_part2_result != [80805]:
    raise Exception()
