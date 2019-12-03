from typing import List, Tuple

wire_paths = [x.split(",") for x in open("day3_input.txt", "r").readlines()]

movement_amounts = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}


def create_path(instructions: List[str]):
    current_pos = (0, 0)
    for movement in instructions:
        direction = movement[0]
        movement_amount: Tuple[int, int] = movement_amounts[direction]
        distance = int(movement[1:])
        for _ in range(distance):
            current_pos = (current_pos[0] + movement_amount[0], current_pos[1] + movement_amount[1])
            yield current_pos


paths = [set(create_path(x)) for x in wire_paths]
intersections = paths[0]
for path in paths[1:]:
    intersections = intersections.intersection(path)

print(
    "Part 1: " +
    str(
        min(
            map(lambda i: abs(i[0]) + abs(i[1]), intersections)
        )
    )
)
