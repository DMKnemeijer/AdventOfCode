import sys
import typing
import numpy as np

DEBUG: bool = False
ALPHABET: str = "abcdefghijklmnopqrstuvwxyz"
HEX: str = "0123456789abcdef"


def logger(log: str, debug: bool = DEBUG) -> None:
    """
    :param str log: Line to pass on to the default Python logger
    :param bool debug: Variable to override global debug variable
    """
    if debug:
        print(log)


def read_input(filename: str, target_type: str = 'str') -> typing.Union[list[str], list[int]]:
    """
    :param str filename: Name of the file
    :param str target_type: Specifies what type of data the function (strings or integers) should return
    :return List of strings from the input file
    :rtype: List[str]
    """
    with open(filename) as f:
        lines = [line.rstrip() for line in f]
        if target_type == 'str':
            return lines
        elif target_type == 'int':
            return list(map(int, lines))


def read_data(filename) -> list[list[str]]:
    with open(filename, "r") as file:
        data = [data.split() for data in file.read().split("\n\n")]
        return data


def read_line(filename: str, target_type: str = 'str') -> typing.Union[list[str], list[int]]:
    line = read_data(filename)[0].split(',')
    if target_type == 'int':
        return list(map(int, line))
    return line


def prod(val: list[int]) -> int:
    """
    :param List[int] val: List of integer values to take the product of
    :return: Product of all the values in the input list of integers
    :rtype: int
    """
    r = 1
    for e in val:
        r *= e
    return r


def pivot(data: list[str]) -> list[list[str]]:
    """
    Given a list of strings with size AxB, return a pivoted list of strings with size BxA

    :param list[str] data: List of strings
    :return: Pivoted list of strings
    :rtype: list[str]
    """
    return [[y[x] for y in data] for x in range(len(data[0]))]


def get_adjacent_values(arr: np.array, x: int, y: int, check_diagonals=False) -> list:
    adjacent_values = []
    x_max, y_max = arr.shape
    # Check above
    if y - 1 >= 0:
        adjacent_values.append(arr[x, y-1])
    # Check right:
    if x + 1 < x_max:
        adjacent_values.append(arr[x+1, y])
    # Check below:
    if y + 1 < y_max:
        adjacent_values.append(arr[x, y+1])
    # Check left:
    if x - 1 >= 0:
        adjacent_values.append(arr[x-1, y])
    if check_diagonals:
        diags = get_diagonal_values(arr, x, y)
        adjacent_values.extend(diags)
    return adjacent_values


def get_diagonal_values(arr, x, y):
    diagonal_values = []
    x_max, y_max = arr.shape
    # Top right
    if y - 1 >= 0 and x + 1 < x_max:
        diagonal_values.append(arr[x + 1, y - 1])
    # Bottom right
    if y + 1 < y_max and x + 1 < x_max:
        diagonal_values.append(arr[x + 1, y + 1])
    # Bottom left
    if y + 1 < y_max and x - 1 >= 0:
        diagonal_values.append(arr[x - 1, y + 1])
    # Top left
    if y - 1 >= 0 and x - 1 >= 0:
        diagonal_values.append(arr[x - 1, y - 1])
    return diagonal_values


def generate_np(raw_input: list[str], nums=False) -> np.array:
    input_list = []
    for row in raw_input:
        line = [int(char) if nums else char for char in row]
        input_list.append(line)
    arr = np.array(input_list)
    logger(f"Generated a new array with size {arr.shape}")
    return arr
