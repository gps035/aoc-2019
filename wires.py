from typing import List

# It is assumed that the path of a single wire does not overlap itself

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


def get_intersections(paths):
    return set.intersection(*[set(point for point, steps in path) for path in paths])


def calculate_closest_intersection_to_origin(wire_paths: List[List[str]]):
    paths = [list(create_path(x)) for x in wire_paths]
    wires_crossed = get_intersections(paths)
    return min([abs(i[0]) + abs(i[1]) for i in wires_crossed])


def calculate_closest_intersection_along_wires(wire_paths: List[List[str]]):
    paths = [list(create_path(x)) for x in wire_paths]
    wires_crossed = get_intersections(paths)

    distances = {}
    for x in paths:
        for point, steps in x:
            if point not in wires_crossed:
                continue
            total = distances.get(point, 0)
            distances[point] = total + steps

    return min([distances[x] for x in wires_crossed])
