"""
Day 1 of the Advent of Code 2020

part 1:
input: file with blocks of lines, each contains 1 number, separated by a blank line
output: the sum of the biggest block

part 2:
output: the sum of the top 3 biggest blocks
"""


def part1():
    """
    takes care of part 1

    reads Day1Input.txt and prints the sum of the biggest block
    according to the rules of part 1

    :return: the sum of the biggest block
    :rtype: int
    """
    with open("Day1Input.txt", "r") as f:
        # we read and evaluates the file's content into a list
        # each block of numbers is stored in a different sub list
        blocks = [[eval(num) for num in block.split("\n")] for block in f.read().split("\n\n")]
    print(max([sum(block) for block in blocks]))


def part2():
    """
    takes care of part 2

    reads Day1Input.txt and prints the sum of the top 3 biggest blocks
    according to the rules of part 2

    :return: the sum of the top 3 biggest blocks
    :rtype: int
    """
    with open("Day1Input.txt", "r") as f:
        # we read and evaluates the file's content into a list
        # each block of numbers' sum is stored into the list which is then sorted
        blocks = sorted([sum([eval(num) for num in block.split("\n")]) for block in f.read().split("\n\n")])
    # pop gets the last value in the list. 3 last ones are the top 3
    print(sum([blocks.pop() for i in range(3)]))


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
