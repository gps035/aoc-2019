from typing import List


def get_value(program: List[int], index: int):
    return program[program[index]]


def set_value(program: List[int], index: int, value: int):
    program[program[index]] = value


def run_program(program: List[int], noun: int, verb: int):
    program = program.copy()
    program[1] = noun
    program[2] = verb
    pc = 0

    while True:
        if program[pc] == 99:
            break
        elif program[pc] == 1:
            result = get_value(program, pc + 1) + get_value(program, pc + 2)
            set_value(program, pc + 3, result)
            pc = pc + 4
            continue
        elif program[pc] == 2:
            result = get_value(program, pc + 1) * get_value(program, pc + 2)
            set_value(program, pc + 3, result)
            pc = pc + 4

    return program[0]


def find_noun_and_verb(expected_result: int, program: List[int]):
    for n in range(0, 99):
        for v in range(0, 99):
            this_output = run_program(program, n, v)
            if this_output == expected_result:
                return (n * 100) + v


op_codes = [int(x) for x in open("day2_input.txt", "r").readline().split(",")]

program_output = run_program(op_codes, 12, 2)
print(f"Part 1: {program_output}")

correct_input = find_noun_and_verb(19690720, op_codes)
print(f"Part 2: {correct_input}")
