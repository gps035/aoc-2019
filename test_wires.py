import unittest

from wires import calculate_closest_intersection_to_origin, calculate_closest_intersection_along_wires


class TestWires(unittest.TestCase):
    def test_closest_to_origin_1(self):
        wire_paths = [['R8', 'U5', 'L5', 'D3'], ['U7', 'R6', 'D4', 'L4']]
        distance = calculate_closest_intersection_to_origin(wire_paths)
        self.assertEqual(distance, 6)

    def test_closest_to_origin_2(self):
        wire_paths = [['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72'],
                      ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']]
        distance = calculate_closest_intersection_to_origin(wire_paths)
        self.assertEqual(distance, 159)

    def test_closest_to_origin_3(self):
        wire_paths = [['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51'],
                      ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7']]
        distance = calculate_closest_intersection_to_origin(wire_paths)
        self.assertEqual(distance, 135)

    def test_closest_along_wires_1(self):
        wire_paths = [['R8', 'U5', 'L5', 'D3'], ['U7', 'R6', 'D4', 'L4']]
        distance = calculate_closest_intersection_along_wires(wire_paths)
        self.assertEqual(distance, 30)

    def test_closest_along_wires_2(self):
        wire_paths = [['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72'],
                      ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']]
        distance = calculate_closest_intersection_along_wires(wire_paths)
        self.assertEqual(distance, 610)

    def test_closest_along_wires_3(self):
        wire_paths = [['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51'],
                      ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7']]
        distance = calculate_closest_intersection_along_wires(wire_paths)
        self.assertEqual(distance, 410)


if __name__ == '__main__':
    unittest.main()
