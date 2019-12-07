from intcode_computer import run_program

op_codes = [int(x) for x in open("day5_input.txt", "r").readline().split(",")]


part1_output = 0
for part1_output in run_program(op_codes.copy(), [1]):
    pass

part2_output = next(run_program(op_codes.copy(), [5]))

print(f"Part 1: {part1_output}")
print(f"Part 2: {part2_output}")

if part1_output != 15508323 or part2_output != 9006327:
    raise Exception()
