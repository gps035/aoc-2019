from typing import List


def run_program(program: List[int], program_input: List[int] = None):
    if not program_input:
        program_input = []

    pc = 0
    ic = 0
    rb = 0

    while True:
        first_value = str(program[pc])

        # Edge case - op code has no modes and is less than 10, therefore no leading 0
        first_value = first_value.zfill(2)

        op_code = first_value[-2:]

        if op_code == "99":
            break

        parameter_modes = first_value[:-2]

        # Edge case - Pad with enough leading 0s (default)  for max number of params
        parameter_modes = parameter_modes.zfill(4)

        def get_param_index(number: int):
            mode = parameter_modes[-number]
            if mode == '0':
                return program[pc + number]
            if mode == '1':
                return pc + number
            if mode == '2':
                return rb + program[pc + number]
            raise Exception()

        def expand_memory(index: int):
            for _ in range(len(program), index + 1):
                program.append(0)
            return index

        def get_param(number: int):
            index = get_param_index(number)
            expand_memory(index)
            return program[index]

        def set_param(number: int, value):
            index = get_param_index(number)
            expand_memory(index)
            program[index] = value

        if op_code == "01":
            result = get_param(1) + get_param(2)
            set_param(3, result)
            pc = pc + 4
        elif op_code == "02":
            result = get_param(1) * get_param(2)
            set_param(3, result)
            pc = pc + 4
        elif op_code == "03":
            set_param(1, program_input[ic])
            ic += 1
            pc = pc + 2
        elif op_code == "04":
            yield get_param(1)
            pc = pc + 2
        elif op_code == "05":
            pc = get_param(2) if get_param(1) != 0 else pc + 3
        elif op_code == "06":
            pc = get_param(2) if get_param(1) == 0 else pc + 3
        elif op_code == "07":
            set_param(3, 1 if get_param(1) < get_param(2) else 0)
            pc = pc + 4
        elif op_code == "08":
            set_param(3, 1 if get_param(1) == get_param(2) else 0)
            pc = pc + 4
        elif op_code == "09":
            rb += get_param(1)
            pc = pc + 2
        else:
            raise Exception()
