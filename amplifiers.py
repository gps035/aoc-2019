import itertools
from typing import List, Tuple

from intcode_computer import run_program

NUMBER_OF_AMPS = 5


def run_amps(program: List[int], phase_settings: Tuple[int, ...]):
    amp_inputs = []
    for amp in range(NUMBER_OF_AMPS):
        amp_inputs.append([phase_settings[amp]])
    amps = []
    for amp in range(NUMBER_OF_AMPS):
        amps.append(run_program(program.copy(), amp_inputs[amp]))
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
