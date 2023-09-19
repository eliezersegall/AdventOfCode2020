"""
Day 4 of the Advent of Code 2022

part 1:
input: a file where each line contains 2 ranges of numbers.
output: the number of lines where 1 range is completely contained by the other

example: consider the following list of range pairs:

2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8

in this example, 2-8 fully contains 3-7, and 6-6 is fully contained by 4-6.
Meaning, there are 2 lines that fulfill the requirements

part 2:
output: the number of lines where the ranges overlap

example: considering the example in part 1:

the first two pairs (2-4,6-8 and 2-3,4-5) don't overlap,
while the remaining four pairs (5-7,7-9, 2-8,3-7, 6-6,4-6, and 2-6,4-8) do overlap:

5-7,7-9 overlaps in a single number, 7.
2-8,3-7 overlaps all numbers from 3 through 7.
6-6,4-6 overlaps in a single number, 6.
2-6,4-8 overlaps in numbers 4, 5, and 6.
So, in this example, the number of lines with overlapping range pairs is 4.
"""


def part1():
    """
    takes care of part 1

    reads Day4Input.txt and counts how many lines have 1 range that contains the other

    :return: the number of lines where 1 range is completely contained by the other
    :rtype: int
    """

    def contained(a_start, a_end, b_start, b_end):
        """
        checks range containment

        receives 2 ranges of numbers - a and b
        checks if a given range is contained in the other

        :param a_start: start of range a
        :param a_end: end of range a
        :param b_start: start of range b
        :param b_end: end of range b
        :return: True if 1 range is contains in the other, otherwise False
        :rtype: bool
        """
        # we first check which range is bigger, and then, we check if it contains the smaller range
        if len(range(a_start, a_end + 1)) > len(range(b_start, b_end + 1)):
            return a_end >= b_end and a_start <= b_start
        return a_end <= b_end and a_start >= b_start

    with open("Day4Input.txt", 'r') as f:
        ranges = [[eval(n) for n in line.replace(',', '-').split('-')] for line in f.read().splitlines()]
    print(sum(1 for line in ranges if contained(line[0], line[1], line[2], line[3])))


def part2():
    """
    takes care of part 2

    reads Day4Input.txt and prints the number of lines where the ranges overlap

    :return: the number of lines where the ranges overlap
    :rtype: int
    """

    def overlaps(a_start, a_end, b_start, b_end):
        """
        checks range containment

        receives 2 ranges of numbers - a and b
        checks if the ranges overlap with each other

        :param a_start: start of range a
        :param a_end: end of range a
        :param b_start: start of range b
        :param b_end: end of range b
        :return: True if there's an overlap between the ranges, otherwise False
        :rtype: bool
        """
        return len(set(range(a_start, a_end + 1)) & set(range(b_start, b_end + 1))) != 0

    with open("Day4Input.txt", 'r') as f:
        ranges = [[eval(n) for n in line.replace(',', '-').split('-')] for line in f.read().splitlines()]
    print(sum(1 for line in ranges if overlaps(line[0], line[1], line[2], line[3])))


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
