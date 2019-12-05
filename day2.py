from typing import List

from intcode_computer import run_program


def update_noun_and_verb(program: List[int], noun: int, verb: int):
    program = program.copy()
    program[1] = noun
    program[2] = verb
    return program


def find_noun_and_verb(expected_result: int, program: List[int]):
    for n in range(0, 99):
        for v in range(0, 99):
            this_output, _ = run_program(update_noun_and_verb(program, n, v))
            if this_output == expected_result:
                return (n * 100) + v


op_codes = [int(x) for x in open("day2_input.txt", "r").readline().split(",")]

program_output, _ = run_program(update_noun_and_verb(op_codes, 12, 2))
correct_input = find_noun_and_verb(19690720, op_codes)

print(f"Part 1: {program_output}")
print(f"Part 2: {correct_input}")

if program_output != 2890696 or correct_input != 8226:
    raise Exception()
