from aoc import aoc


def sonar_sweep(depth_list: list[str], window: int) -> int:
    """
    :param list[str] depth_list: list of strings containing the depth values of the sonar
    :param int window: Number that indicates how many values should be taken into account as a sliding window
    :return: Number of values that have an increased depth
    :rtype: int
    """
    return sum([1 for i in range(window, len(depth_list)) if int(depth_list[i]) > int(depth_list[i - window])])


input = aoc.read_input('../input/in.txt')

print(sonar_sweep(input, 1))
print(sonar_sweep(input, 3))
