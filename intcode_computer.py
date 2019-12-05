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
