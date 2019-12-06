from dataclasses import dataclass
from typing import List, Optional

orbits = [line.rstrip("\n").split(")") for line in open('day6_input.txt', "r").readlines()]


@dataclass
class Node:
    name: str
    parent: Optional["Node"]
    children: List["Node"]
    indirect_parents: int

    def is_com(self):
        return self.parent is None

    def path_to_com(self):
        me_to_com = [self]
        while not me_to_com[-1].is_com():
            me_to_com.append(me_to_com[-1].parent)
        return me_to_com

    def transfers_to(self, obj2: "Node"):
        me_to_com = self.path_to_com()
        common_ancestor = obj2
        while common_ancestor not in me_to_com:
            common_ancestor = common_ancestor.parent
        return (obj2.indirect_parents - common_ancestor.indirect_parents - 1) + \
               (self.indirect_parents - common_ancestor.indirect_parents - 1)

    def update_indirect_parents(self):
        if self.is_com():
            return
        me_to_com = self.path_to_com()
        self.indirect_parents = len(me_to_com) - 2


# Build graph, and index on name

orbit_details = {}

for orbit in orbits:
    centre = orbit[0]
    moon = orbit[1]
    if centre not in orbit_details:
        orbit_details[centre] = Node(centre, None, [], 0)
    if moon not in orbit_details:
        orbit_details[moon] = Node(moon, None, [], 0)
    orbit_details[centre].children.append(orbit_details[moon])
    orbit_details[moon].parent = orbit_details[centre]

for obj in orbit_details.values():
    obj.update_indirect_parents()

# Calculate results

indirect_orbits = sum(x.indirect_parents for x in orbit_details.values())
direct_orbits = sum(1 for _ in (x for x in orbit_details.values() if not x.is_com()))

part1_output = direct_orbits + indirect_orbits

part2_output = orbit_details["YOU"].transfers_to(orbit_details["SAN"])

print(f"Part 1: {part1_output}")
print(f"Part 2: {part2_output}")

if part1_output != 249308 or part2_output != 349:
    raise Exception()
