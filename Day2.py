"""
Day 2 of the Advent of Code 2022

part 1:
input: lines of the format 'a b' where a ∈ {'A', 'B', 'C'}, b ∈ {'X', 'Y', 'Z'}
each letter stands for either rock, paper or scissors.
'A' and 'X' stands for rock,
'B' and 'Y' stands for paper,
'C' and 'Z' stands for scissors.
each line shows a match of rock-paper-scissors. our job is to calculate the points of the RIGHT player (b column).
Scoring rules:
choosing rock grants 1 point. Paper is worth 2 points, and scissors are 3 points worth.
Winning grants 6 points. A draw grants 3 points and losing grants 0 points.
output: The right player's final score after all matches.

example: consider the following file:
A Y
B X
C Z
This strategy guide predicts and recommends the following:

In the first round, left player chose Rock (A), and right player chose Paper (Y).
This ended in a win with a score of 8 (2 because right player chose Paper + 6 because right player won).
In the second round, left player chose Paper (B), and right player chose Rock (X).
This ended in a loss for right player with a score of 1 (1 + 0).
The third round is a draw with both players choosing Scissors, giving right player a score of 3 + 3 = 6.
In this example, right player got a total score of 15 (8 + 1 + 6).



part 2:
the input is the same as part 1 but the meaning of the letter b is different.
'X' means that player b lost the match,
'Y' means that the match was a draw,
'Z' means that player b won the match.
Scoring rules are the same as part 1.
output: The right player's final score after all matches.

example: considering the same file from part 1's example:
In the first round, left player chose Rock (A), and round has ended in a draw (Y), so right player also chose Rock.
This gives right player a score of 1 + 3 = 4.
In the second round, left player chose Paper (B), and right player lost (X), which means right player chose Rock,
ending with a score of 1 + 0 = 1.
In the third round, right player defeated left player's Scissors with Rock for a score of 1 + 6 = 7.
Meaning right player got a total score of 12.
"""


def part1():
    """
    takes care of part 1

    reads Day2Input.txt and prints the sum of the scores of all matches
    according to the rules of part 1

    :return: the sum of the scores of all matches
    :rtype: int
    """

    def score_part1(a, b):
        """
        calculates the score of a match between a and b

        The score is calculated for the right player (b)
        according to the scoring rules mentioned above.
        The calculation is done as follows:
        The ascii value of a is between 65 and 67 (inclusive) for rock, paper and scissors respectively.
        and the ascii value of b is between 88 and 90 (inclusive) for rock, paper and scissors respectively.
        Therefore, the difference between the ascii values of a and b ('b' - 'a') is:
        23 in case of a draw ; 24 or 21 in case of a win ; 22 or 25 in case of a loss.
        meaning that the difference between the ascii values of a and b modulo 3 is:
        2 in case of a draw ; 0 in case of a win ; 1 in case of a loss.
        Therefore, the score of the match is calculated based on the result of the modulo operation.
        Additionally, the score is increased by the ascii value of b modulo 87,
        which is 1 for rock, 2 for paper and 3 for scissors.

        :param a: the left player's choice
        :type a: str

        :param b: the right player's choice
        :type b: str

        :return: the score of the match
        :rtype: int
        """

        match_result = (ord(b) - ord(a)) % 3
        match_score = 6 if match_result == 0 else 3 if match_result == 2 else 0
        return ord(b) % 87 + match_score

    with open("Day2Input.txt", 'r') as f:
        # we read the file's content into a list of sub lists
        # each sub list contains the left player's choice and the right player's choice
        matches = [[match[0], match[-1]] for match in f.read().splitlines()]
    print(sum([score_part1(match[0], match[1]) for match in matches]))


def part2():
    """
    takes care of part 2

    reads Day2Input.txt and prints the sum of the scores of all matches
    according to the rules of part 2

    :return: the sum of the scores of all matches
    :rtype: int
    """

    def score_part2(a, b):
        """
        calculates the score of a match between a and b

        The score is calculated for the right player (b)
        according to the scoring rules mentioned above
        and based on the instructions of part 2

        :param a: the left player's choice
        :type a: str

        :param b: the match's result
        :type b: str

        :return: the score of the match
        :rtype: int
        """

        def element_score():
            """
            calculates the element point bonus

            calculation is based on b and the instructions
            of part 2

            :return: element point bonus
            :rtype: int
            """

            def win():
                """
                calculates the element point bonus in case of a win

                a has the value of its ascii number modulo 64
                So, the element b chose has that value + 1 unless a is scissors
                which means b's element is rock thus worth 1 point

                :return: element point bonus
                :rtype: int
                """
                temp = (ord(a) % 64) + 1
                return temp if temp <= 3 else 1

            def lose():
                """
                calculates the element point bonus in case of losing

                a has the value of its ascii number modulo 64
                So, the element b chose has that value - 1 unless a is rock
                which means b's element is scissors thus worth 3 point

                :return: element point bonus
                :rtype: int
                """
                temp = (ord(a) % 64) - 1
                return temp if temp > 0 else 3

            def draw():
                """
                calculates the element point bonus in case of a draw

                a has the value of its ascii number modulo 64
                So, the element b chose has that same value

                :return: element point bonus
                :rtype: int
                """
                return ord(a) % 64

            return win() if b == 'Z' else lose() if b == 'X' else draw()

        # match score is b's ascii value % 88 * 3 (0 for 'X'-lose, 3 for 'Y'-draw and 6 for 'Z'-win)
        return (ord(b) % 88) * 3 + element_score()

    with open("Day2Input.txt", 'r') as f:
        # we read the file's content into a list of sub lists
        # each sub list contains the left player's choice and the right player's choice
        matches = [[match[0], match[-1]] for match in f.read().splitlines()]
    print(sum([score_part2(match[0], match[1]) for match in matches]))


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
