"""
Day 1 of the Advent of Code 2022

part 1:
input: file with blocks of lines, each contains 1 number, separated by a blank line
output: the sum of the biggest block

example: consider the following file:
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000

This list represents 5 blocks:

The first block is 1000, 2000, and 3000, a total of 6000.
The second block is 4000.
The third block is 5000 and 6000, a total of 11000.
The fourth block is 7000, 8000, and 9000, a total of 24000.
The fifth Elf is block is 10000.
In that case the sum of the biggest block is 24000 (fourth block)

part 2:
output: the sum of the top 3 biggest blocks

example:
considering the example from part 1, the 3 biggest blocks are:
The fourth block with a total of 24000
the third block with a total of 11000
the fifth block with a total of 10000
which means the sum is 45000
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
