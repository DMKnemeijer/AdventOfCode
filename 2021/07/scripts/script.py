from aoc import aoc
import statistics as s


def gauss_sum(x: int):
    return (x*(x+1))/2


def crab_alignment(crabs: list[int], exponential: bool = False):
    median_crab = s.median(crabs)
    if exponential:
        aligned_crabs = int(min([sum([gauss_sum(abs(x - target)) for x in crabs]) for target in range(max(crabs))]))
    else:
        aligned_crabs = int(sum([abs(x - median_crab) for x in crabs]))
    return aligned_crabs



input = list(map(int, aoc.read_input('../input/in.txt')[0].split(',')))

print(crab_alignment(input))
print(crab_alignment(input, True))




