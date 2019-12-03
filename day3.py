from typing import List, Tuple

wire_paths = [x.split(",") for x in open("day3_input.txt", "r").readlines()]

movement_amounts = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}


def create_path(instructions: List[str]):
    current_pos = (0, 0)
    steps = 0
    for movement in instructions:
        direction = movement[0]
        movement_amount: Tuple[int, int] = movement_amounts[direction]
        distance = int(movement[1:])
        for _ in range(distance):
            current_pos = (
                current_pos[0] + movement_amount[0],
                current_pos[1] + movement_amount[1]
            )
            steps += 1
            yield current_pos, steps


# It is assumed that the path of a single wire does not overlap itself
paths = []
distances = {}

for x in wire_paths:
    seen = set()
    for point, steps in create_path(x):
        if point not in distances.keys():
            distances[point] = 0
        seen.add(point)
        distances[point] += steps
    paths.append(seen)

intersections = paths[0]
for x in paths[1:]:
    intersections = intersections.intersection(x)

print(f"Part 1: {min([abs(i[0]) + abs(i[1]) for i in intersections])}")

print(f"Part 2: {min([distances[x] for x in intersections])}")
