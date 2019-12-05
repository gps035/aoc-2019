from typing import List

wire_paths = [x.split(",") for x in open("day3_input.txt", "r").readlines()]

step_vectors = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}


def create_path(instructions: List[str]):
    current_pos = (0, 0)
    steps = 0
    for movement in instructions:
        direction = movement[0]
        distance = int(movement[1:])
        step_vector = step_vectors[direction]
        for _ in range(distance):
            new_x = current_pos[0] + step_vector[0]
            new_y = current_pos[1] + step_vector[1]
            current_pos = (new_x, new_y)
            steps += 1
            yield current_pos, steps


# It is assumed that the path of a single wire does not overlap itself
paths = [list(create_path(x)) for x in wire_paths]
path_points = [set(point for point, steps in path) for path in paths]
wires_crossed = set.intersection(*path_points)

distances = {}
for x in paths:
    for point, steps in x:
        if point not in wires_crossed:
            continue
        total = distances.get(point, 0)
        distances[point] = total + steps

shortest_distance_to_origin = min([abs(i[0]) + abs(i[1]) for i in wires_crossed])
shortest_distance_along_wires = min([distances[x] for x in wires_crossed])

print(f"Part 1: {shortest_distance_to_origin}")
print(f"Part 2: {shortest_distance_along_wires}")

if shortest_distance_to_origin != 865 or shortest_distance_along_wires != 35038:
    raise Exception()
