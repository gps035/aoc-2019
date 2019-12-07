import unittest

from orbits import count_total_orbits, orbital_transfers_required


class TestOrbits(unittest.TestCase):
    def test_count_orbits(self):
        orbit_map = ["COM)B", "B)C", "C)D", "D)E", "E)F", "B)G", "G)H", "D)I", "E)J", "J)K", "K)L"]
        self.assertEqual(count_total_orbits(orbit_map), 42)

    def test_orbital_transfers_required(self):
        orbit_map = ["COM)B", "B)C", "C)D", "D)E", "E)F", "B)G", "G)H", "D)I", "E)J", "J)K", "K)L", "K)YOU", "I)SAN"]
        self.assertEqual(orbital_transfers_required(orbit_map, "YOU", "SAN"), 4)


if __name__ == '__main__':
    unittest.main()
