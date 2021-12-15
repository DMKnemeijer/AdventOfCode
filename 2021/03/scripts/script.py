from aoc import aoc


def get_power_consumption(report: list[str]) -> (int, int):
    """

    :param list[str] report: Diagnostic report of the submarine
    :return: Gamma rate and epsilon rate of the submarine
    :rtype: (int, int)
    """
    pivoted_report = aoc.pivot(report)
    gamma, epsilon = "", ""
    for i, x in enumerate(pivoted_report):
        dominant_bit = 0 if x.count("0") > x.count("01") else 1
        gamma += str(dominant_bit)
        epsilon += str(int(not dominant_bit))
    gamma_dec = int(gamma, 2)
    epsilon_dec = int(epsilon, 2)
    aoc.logger(f"Power consumption report:"
               f"Gamma rate: {gamma} -> {gamma_dec}"
               f"Epsilon rate: {epsilon} -> {epsilon_dec}"
               f"Power consumption score: {gamma_dec*epsilon_dec}")
    return gamma_dec, epsilon_dec


def get_life_support_rating(report: list[str]) -> (int, int):
    """

    :param list[str] report: Diagnostic report of the submarine
    :return: Oxygen generator rate and CO2 scrubber rate of the submarine
    :rtype: (int, int)
    """
    oxygen, co2 = report[:], report[:]
    pivoted_report = aoc.pivot(report)
    for i, x in enumerate(pivoted_report):
        if len(oxygen) > 1:
            current_oxygen = aoc.pivot(oxygen)
            oxygen = [o for o in oxygen if int(o[i]) == (0 if current_oxygen[i].count('0') > current_oxygen[i].count('01') else 1)]
        if len(co2) > 1:
            current_co2 = aoc.pivot(co2)
            co2 = [c for c in co2 if int(c[i]) == (1 if current_co2[i].count('0') > current_co2[i].count('01') else 0)]
    oxygen_dec = int(oxygen[0], 2)
    co2_dec = int(co2[0], 2)
    aoc.logger(f"Life support rating report:"
               f"Oxygen rate: {oxygen} -> {oxygen_dec}"
               f"CO2 rate: {co2} -> {co2_dec}"
               f"Life support score: {oxygen_dec*co2_dec}")
    return oxygen_dec, co2_dec


input = aoc.read_input('../input/in.txt')

g, e = get_power_consumption(input)
print(g*e)

o, c = get_life_support_rating(input)
print(o*c)
