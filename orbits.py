from dataclasses import dataclass
from typing import Optional, List


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


def build_indexed_graph(orbit_map: List[str]):
    orbit_details = {}

    for orbit in orbit_map:
        parts = orbit.split(")")
        centre = parts[0]
        moon = parts[1]
        if centre not in orbit_details:
            orbit_details[centre] = Node(centre, None, [], 0)
        if moon not in orbit_details:
            orbit_details[moon] = Node(moon, None, [], 0)
        orbit_details[centre].children.append(orbit_details[moon])
        orbit_details[moon].parent = orbit_details[centre]

    for obj in orbit_details.values():
        obj.update_indirect_parents()
    return orbit_details


def count_total_orbits(orbit_map: List[str]):
    orbit_details = build_indexed_graph(orbit_map)
    indirect_orbits = sum(x.indirect_parents for x in orbit_details.values())
    direct_orbits = sum(1 for _ in (x for x in orbit_details.values() if not x.is_com()))
    return direct_orbits + indirect_orbits


def orbital_transfers_required(orbit_map: List[str], current: str, destination: str):
    orbit_details = build_indexed_graph(orbit_map)
    return orbit_details[current].transfers_to(orbit_details[destination])
