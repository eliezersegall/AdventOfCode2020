"""
Day 6 of the Advent of Code 2022

input: a file that contains a string of characters

part 1:
we need to find the first sequence of four characters that are all different.
output: the serial number of the last character from the sequence

examples:
input: bvwbjplbgvbhsrlpgdmjqwftvncz - output: 5
input: nppdvjthqldpwncqszvftbrmjlhg - output: 6
input: nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg - output: 10
input: zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw - output: 11


part 2:
This time, we need to find the first sequence of 14 characters that are all different.
output: the serial number of the last character from the sequence

examples:
input: bvwbjplbgvbhsrlpgdmjqwftvncz - output: 23
input: nppdvjthqldpwncqszvftbrmjlhg - output: 23
input: nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg - output: 29
input: zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw - output: 26
"""


def part1():
    """
    takes care of part 1

    reads Day6Input.txt and finds the first sequence of four characters that are all different.

    :return: the serial number of the last character from the sequence
    :rtype: int
    """
    with open("Day6Input.txt", 'r') as f:
        f_str = f.read()
    # we check each quartet by using a generator since we don't need all occurrences
    # we print the index of the last char of the first quartet + 1 since we count from 0
    sequences = (i + 1 for i in range(3, len(f_str)) if
                 len(set(f_str[i - 3:i + 1:])) == 4)
    print(next(sequences))


def part2():
    """
    takes care of part 2

    reads Day6Input.txt and finds the first sequence of four characters that are all different.

    :return: the serial number of the last character from the sequence
    :rtype: int
    """
    with open("Day6Input.txt", 'r') as f:
        f_str = f.read()
    # we check each 14 chars substring by a using generator since we don't need all occurrences
    # we print the index of the last char of the first fitting substring + 1 since we count from 0
    sequences = (i + 1 for i in range(13, len(f_str)) if
                 len(set(f_str[i - 13:i + 1:])) == 14)
    print(next(sequences))


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
