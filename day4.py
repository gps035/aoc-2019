min = 178416
max = 676461

part_1_total = 0
part_2_total = 0

for candidate in range(min, max + 1):
    candidate_str = str(candidate)
    double = False
    exact_double = False
    ascending = True
    for i in range(1, len(candidate_str)):
        current = candidate_str[i]
        last = candidate_str[i - 1]
        next = None if i + 1 == len(candidate_str) else candidate_str[i + 1]
        next_last = None if i == 1 else candidate_str[i - 2]
        if current < last:
            ascending = False
            break
        if current == last:
            double = True
            if next_last != current and next != current:
                exact_double = True
    if ascending and double:
        part_1_total += 1
        if exact_double:
            part_2_total += 1

print(f"Part 1: {part_1_total}")
print(f"Part 2: {part_2_total}")

if part_1_total != 1650 or part_2_total != 1129:
    raise Exception()
