import itertools
from typing import Tuple, List

from intcode_computer import run_program

NUMBER_OF_AMPS = 5
op_codes = [int(x) for x in open("day7_input.txt", "r").readline().split(",")]


def run_amps(phase_settings: Tuple[int, ...]):
    amp_inputs = []
    for amp in range(NUMBER_OF_AMPS):
        amp_inputs.append([phase_settings[amp]])
    amps = []
    for amp in range(NUMBER_OF_AMPS):
        amps.append(run_program(op_codes.copy(), amp_inputs[amp]))
    next_amp_input = 0
    current_amp = 0
    while True:
        amp_inputs[current_amp].append(next_amp_input)
        output = next(amps[current_amp], None)
        if output is None:
            break
        next_amp_input = output
        current_amp = (current_amp + 1) % NUMBER_OF_AMPS
    return next_amp_input


def get_best_phase_setting_output(candidate_phase_settings: List[Tuple[int, ...]]):
    best_output = 0
    for phase_settings in candidate_phase_settings:
        output = run_amps(phase_settings)
        if output > best_output:
            best_output = output
    return best_output


part1_output = get_best_phase_setting_output(
    list(itertools.permutations([0, 1, 2, 3, 4], NUMBER_OF_AMPS))
)
part2_output = get_best_phase_setting_output(
    list(itertools.permutations([5, 6, 7, 8, 9], NUMBER_OF_AMPS))
)

print(f"Part 1: {part1_output}")
print(f"Part 2: {part2_output}")

if part1_output != 116680 or part2_output != 89603079:
    raise Exception()
