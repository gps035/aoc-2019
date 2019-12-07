from typing import List

from intcode_computer import run_program

op_codes = [int(x) for x in open("day2_input.txt", "r").readline().split(",")]


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


part1_output = run_program_with_noun_and_verb(op_codes, 12, 2)
part2_output = find_noun_and_verb(19690720, op_codes)

print(f"Part 1: {part1_output}")
print(f"Part 2: {part2_output}")

if part1_output != 2890696 or part2_output != 8226:
    raise Exception()
