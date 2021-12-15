from aoc import aoc

input = aoc.read_input('../input/in.txt')
fishies = list(map(int, input[0].split(',')))


def simulate_school(fish, days):
    school = [0 for _ in range(9)]
    for f in fish:
        school[f] += 1
    for i in range(days):
        aoc.logger(f"Current day: {i}, {days-i} left to go")
        new_school = [0 for _ in range(9)]
        for day, amount in enumerate(school):
            if day == 0:
                new_school[6] += amount
                new_school[8] += amount
            else:
                new_school[day-1] += amount
        school = new_school
    return sum(school)


print(simulate_school(fishies, 80))
print(simulate_school(fishies, 256))




