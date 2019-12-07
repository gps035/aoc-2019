import unittest

from intcode_computer import run_program


class TestIntCodeComputer(unittest.TestCase):
    def test_program_modification_1(self):
        program = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
        for _ in run_program(program):
            pass
        self.assertEqual(program[0], 3500)

    def test_program_modification_2(self):
        program = [1, 0, 0, 0, 99]
        for _ in run_program(program):
            pass
        self.assertEqual(program[0], 2)

    def test_program_modification_3(self):
        program = [2, 4, 4, 5, 99, 0]
        for _ in run_program(program):
            pass
        self.assertEqual(program[5], 9801)

    def test_program_modification_4(self):
        program = [1, 1, 1, 4, 99, 5, 6, 0, 99]
        for _ in run_program(program):
            pass
        self.assertEqual(program[0], 30)

    def test_program_modification_immediate_1(self):
        program = [1002, 4, 3, 4, 33]
        for _ in run_program(program):
            pass
        self.assertEqual(program[4], 99)

    def test_echo_1(self):
        program_input = [1]
        output = list(run_program([3, 0, 4, 0, 99], program_input))
        self.assertEqual(output, program_input)

    def test_echo_2(self):
        program_input = [2]
        output = list(run_program([3, 0, 4, 0, 99], program_input))
        self.assertEqual(output, program_input)

    def test_echo_3(self):
        program_input = [2]
        output = list(run_program([3, 0, 4, 0, 99], program_input))
        self.assertEqual(output, program_input)

    def test_equal_to_8_position_1(self):
        program = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
        output = list(run_program(program, [7]))
        self.assertEqual(output, [0])

    def test_equal_to_8_position_2(self):
        program = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
        output = list(run_program(program, [8]))
        self.assertEqual(output, [1])

    def test_equal_to_8_position_3(self):
        program = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
        output = list(run_program(program, [9]))
        self.assertEqual(output, [0])

    def test_less_than_8_position_1(self):
        program = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
        output = list(run_program(program, [7]))
        self.assertEqual(output, [1])

    def test_less_than_8_position_2(self):
        program = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
        output = list(run_program(program, [8]))
        self.assertEqual(output, [0])

    def test_less_than_8_position_3(self):
        program = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
        output = list(run_program(program, [9]))
        self.assertEqual(output, [0])

    def test_equal_to_8_immediate_1(self):
        program = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
        output = list(run_program(program, [7]))
        self.assertEqual(output, [0])

    def test_equal_to_8_immediate_2(self):
        program = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
        output = list(run_program(program, [8]))
        self.assertEqual(output, [1])

    def test_equal_to_8_immediate_3(self):
        program = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
        output = list(run_program(program, [9]))
        self.assertEqual(output, [0])

    def test_less_than_8_immediate_1(self):
        program = [3, 3, 1107, -1, 8, 3, 4, 3, 99]
        output = list(run_program(program, [7]))
        self.assertEqual(output, [1])

    def test_less_than_8_immediate_2(self):
        program = [3, 3, 1107, -1, 8, 3, 4, 3, 99]
        output = list(run_program(program, [8]))
        self.assertEqual(output, [0])

    def test_less_than_8_immediate_3(self):
        program = [3, 3, 1107, -1, 8, 3, 4, 3, 99]
        output = list(run_program(program, [9]))
        self.assertEqual(output, [0])

    def test_jump_position_1(self):
        program = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
        output = list(run_program(program, [0]))
        self.assertEqual(output, [0])

    def test_jump_position_2(self):
        program = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
        output = list(run_program(program, [1]))
        self.assertEqual(output, [1])

    def test_jump_position_3(self):
        program = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
        output = list(run_program(program, [3]))
        self.assertEqual(output, [1])

    def test_jump_immediate_1(self):
        program = [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]
        output = list(run_program(program, [0]))
        self.assertEqual(output, [0])

    def test_jump_immediate_2(self):
        program = [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]
        output = list(run_program(program, [1]))
        self.assertEqual(output, [1])

    def test_jump_immediate_3(self):
        program = [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]
        output = list(run_program(program, [3]))
        self.assertEqual(output, [1])

    def test_3_way_comparison_1(self):
        program = [
            3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31, 1106, 0, 36, 98, 0, 0, 1002, 21, 125,
            20, 4, 20, 1105, 1, 46, 104, 999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99
        ]
        output = list(run_program(program, [6]))
        self.assertEqual(output, [999])

    def test_3_way_comparison_2(self):
        program = [
            3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31, 1106, 0, 36, 98, 0, 0, 1002, 21, 125,
            20, 4, 20, 1105, 1, 46, 104, 999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99
        ]
        output = list(run_program(program, [7]))
        self.assertEqual(output, [999])

    def test_3_way_comparison_3(self):
        program = [
            3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31, 1106, 0, 36, 98, 0, 0, 1002, 21, 125,
            20, 4, 20, 1105, 1, 46, 104, 999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99
        ]
        output = list(run_program(program, [8]))
        self.assertEqual(output, [1000])

    def test_3_way_comparison_4(self):
        program = [
            3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31, 1106, 0, 36, 98, 0, 0, 1002, 21, 125,
            20, 4, 20, 1105, 1, 46, 104, 999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99
        ]
        output = list(run_program(program, [9]))
        self.assertEqual(output, [1001])

    def test_3_way_comparison_5(self):
        program = [
            3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31, 1106, 0, 36, 98, 0, 0, 1002, 21, 125,
            20, 4, 20, 1105, 1, 46, 104, 999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99
        ]
        output = list(run_program(program, [10]))
        self.assertEqual(output, [1001])


if __name__ == '__main__':
    unittest.main()
