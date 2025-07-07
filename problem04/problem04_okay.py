FILE_NAME = "input.txt"

def read_lines():
    lines = []
    with open(FILE_NAME) as f:
        for line in f:
            lines.append([int(v) for v in line.split()])
    return lines


def is_safe_report(values):
    all_increasing = True
    all_decreasing = True
    difs_ok = True
    pairs = list(zip(values, values[1:]))
    for prev, next in pairs:
        all_increasing = all_increasing and next > prev
        all_decreasing = all_decreasing and next < prev
        dif = abs(prev - next)
        difs_ok = difs_ok and dif >= 1 and dif <= 3
    return (all_increasing or all_decreasing) and difs_ok


def resolve_problem_1(lines):
    safe_reports = 0
    for line in lines:
        if is_safe_report(line):
            safe_reports += 1
    print(safe_reports)


def resolve_problem_2(lines):
    safe_reports = 0
    for line in lines:
        if is_safe_report(line):
            safe_reports += 1
        else:
            safe_permutations = 0
            for i in range(len(line)):
                permutation = [*line]
                del permutation[i]
                if is_safe_report(permutation):
                    safe_permutations += 1
            if safe_permutations > 0:
                safe_reports += 1
    print(safe_reports)


lines = read_lines()
resolve_problem_1(lines)
resolve_problem_2(lines)