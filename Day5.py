"""
Day 5 of the Advent of Code 2022

input: a file that has 2 parts.
On the first part there's a diagram of several piles (columns) of crates
each crate is presented as '[x]' where x is a letter.
below the piles, there is a line with their serial numbers (like in the given example)
The second part contains instructions of moving crates between piles.
Each instruction is a line with the format: 'move x from y to z'
where:  x - how many crates to move
        y - the number of the pile we move the crates from.
        z - the number of the pile we move the crates to.
note that when moving several crates, it means they are moved 1 by 1 and not as a block!

part 1:
we need to find out how the piles look after all instructions have been made
output: a string made of all the top crates' letters.

example: given the next diagram and instruction:
[D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 2 from 1 to 3

The final result will be:

        [N]
    [C] [D]
[Z] [M] [P]
 1   2   3


part 2:
A minor change, when moving several crates, it means they are moved as a block!
meaning they stay in the same order
output: a string made of all the top crates' letters based of course, on the new change

example: given the next diagram and instruction:
[D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 2 from 1 to 3

The final result will be:

        [D]
    [C] [N]
[Z] [M] [P]
 1   2   3
"""
import re
from functools import reduce


def part1():
    """
    takes care of part 1

    reads Day5Input.txt and makes 2 lists. 1st is a list of all piles
    2nd is a list of all instructions

    :return: the string made of all the top crates' letters after piles are complete
    :rtype: str
    """

    def instructions_exe(_piles, _instructions):
        """
        executes the instructions on the piles

        recursive function.
        each time, 1 instruction is executed and the func is recalled with the new arranged piles
        and the instructions list minus the 1 who's got executed
        This is to maintain the principals of pure functional programming

        :param _piles: the piles at their current state of the iteration
        :param _instructions: the instructions list based on the current state of the iteration
        :return: the piles once the instructions are done, otherwise we recall the func
        :rtype: list
        """
        if len(_instructions) == 0:
            return _piles
        # we extract the first instruction in line
        instruction = _instructions[0]
        # we extract the crates that are needed to be moving and already arrange them properly
        to_move = list(reversed(_piles[instruction[1]][-instruction[0]::]))
        # we then add them to the right pile
        to_pile = _piles[instruction[2]] + to_move
        # we update the pile of which we took the crates
        from_pile = _piles[instruction[1]][:-instruction[0]:]
        # we reassemble the piles so that the 2 piles that were included in the instruction's execution
        # are updated
        temp_new_piles = [from_pile if i == instruction[1] else to_pile if i == instruction[2] else _piles[i] for i in
                          range(len(_piles))]
        # func is recalled with 1 instruction less and the newly arranged piles
        return instructions_exe(temp_new_piles, _instructions[1::])

    def remove_last_element(input_list):
        return input_list[:-1:]

    with open("Day5Input.txt", 'r') as f:
        # data will split the file into the diagram part and the instructions part
        data = f.read().split(' 1   2   3   4   5   6   7   8   9 \n\n')
        # piles take first part of data, making an ordered list of the piles
        # based on the input format, the letters appear on each cell from 1 with jumps of 4 (1,5,9..)
        # for each cell i, we store all lines[i]'s chars to construct a pile.
        # we then filter out empty chars (' ') and reverse each sublist to receive the correct pile
        # I added 1 fake pile so we would address the piles with their actual serial number
        piles = ['X'] + [list(filter(lambda x: x != ' ', reversed([line[i] for line in data[0].splitlines()]))) for i in
                         range(1, 35, 4)]
        # instructions are made into a list where each instruction is a trio of the numbers
        # from the original instruction. first element in each sublist is x, then y and z (see line 9)
        # the regular expression gives back all sequences of digits in the original string
        instructions = [[eval(n) for n in re.findall(r'\d+', line)] for line in data[1].splitlines()]
        new_piles = instructions_exe(piles, instructions)
        # we now gather all top crates' letters
        print(reduce(lambda x, y: x + y, [letter[-1] for letter in new_piles[1::]]))


def part2():
    """
    takes care of part 2

    reads Day5Input.txt and makes 2 lists. 1st is a list of all piles
    2nd is a list of all instructions

    :return: the string made of all the top crates' letters after piles are complete
    :rtype: str
    """

    def instructions_exe(_piles, _instructions):
        """
        executes the instructions on the piles

        recursive function.
        each time, 1 instruction is executed and the func is recalled with the new arranged piles
        and the instructions list minus the 1 who's got executed
        This is to maintain the principals of pure functional programming

        :param _piles: the piles at their current state of the iteration
        :param _instructions: the instructions list based on the current state of the iteration
        :return: the piles once the instructions are done, otherwise we recall the func
        :rtype: list
        """
        if len(_instructions) == 0:
            return _piles
        # we extract the first instruction in line
        instruction = _instructions[0]
        # we extract the crates that are needed to be moving and already arrange them properly
        # NOTE: this is the only change from part 1 as we DON'T use reversed()
        to_move = list(_piles[instruction[1]][-instruction[0]::])
        # we then add them to the right pile
        to_pile = _piles[instruction[2]] + to_move
        # we update the pile of which we took the crates
        from_pile = _piles[instruction[1]][:-instruction[0]:]
        # we reassemble the piles so that the 2 piles that were included in the instruction's execution
        # are updated
        temp_new_piles = [from_pile if i == instruction[1] else to_pile if i == instruction[2] else _piles[i] for i in
                          range(len(_piles))]
        # func is recalled with 1 instruction less and the newly arranged piles
        return instructions_exe(temp_new_piles, _instructions[1::])

    def remove_last_element(input_list):
        return input_list[:-1:]

    with open("Day5Input.txt", 'r') as f:
        # data will split the file into the diagram part and the instructions part
        data = f.read().split(' 1   2   3   4   5   6   7   8   9 \n\n')
        # piles take first part of data, making an ordered list of the piles
        # based on the input format, the letters appear on each cell from 1 with jumps of 4 (1,5,9..)
        # for each cell i, we store all lines[i]'s chars to construct a pile.
        # we then filter out empty chars (' ') and reverse each sublist to receive the correct pile
        # I added 1 fake pile so we would address the piles with their actual serial number
        piles = ['X'] + [list(filter(lambda x: x != ' ', reversed([line[i] for line in data[0].splitlines()]))) for i in
                         range(1, 35, 4)]
        # instructions are made into a list where each instruction is a trio of the numbers
        # from the original instruction. first element in each sublist is x, then y and z (see line 9)
        # the regular expression gives back all sequences of digits in the original string
        instructions = [[eval(n) for n in re.findall(r'\d+', line)] for line in data[1].splitlines()]
        new_piles = instructions_exe(piles, instructions)
        # we now gather all top crates' letters
        print(reduce(lambda x, y: x + y, [letter[-1] for letter in new_piles[1::]]))


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
