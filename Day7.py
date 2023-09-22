"""
Day 6 of the Advent of Code 2022

input: a file that presents a resulting terminal output whose syntax is VERY similar to linux terminal.
We basically have a tree of directories of which we can move up and down very much like in linux.
The root directory is '/'.
All lines are from 1 of the following formats:
1.  Lines that begin with $ are commands executed by user.
    Optional commands:
    'cd' means change directory. This changes which directory is the current directory,
    but the specific result depends on the argument:
    'cd x' moves in one level: it looks in the current directory for the directory named x and makes it the current directory.
    'cd ..' moves out one level: it finds the directory that contains the current directory,
    then makes that directory the current directory.
    'cd /' switches the current directory to the outermost directory, the root - '/'.
    'ls' means list, explained in the next line.
2.  Lines that don't begin with $ are the output of the command 'ls'
    as said previously, 'ls' means list. It prints out all the files and directories
    immediately contained by the current directory which can diverse into 2 possible line formats:
    '123 abc' means that the current directory contains a file named abc with size 123.
    'dir xyz' means that the current directory contains a directory named xyz.


part 1:
Based on the information we have from the input, we need to determine the size of each directory.
The size of each directory is the sum of all the files it contains, directly or indirectly.
Then, we need to find out which directories has a total sum that is at most 100000.
Output: the total size of all directories that has a total size of 100000 or less.

example: consider the following file:
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k


Given the commands and output in the example above, we can determine that the filesystem looks visually like this:

- / (dir)
  - a (dir)
    - e (dir)
      - i (file, size=584)
    - f (file, size=29116)
    - g (file, size=2557)
    - h.lst (file, size=62596)
  - b.txt (file, size=14848514)
  - c.dat (file, size=8504156)
  - d (dir)
    - j (file, size=4060174)
    - d.log (file, size=8033020)
    - d.ext (file, size=5626152)
    - k (file, size=7214296)

The total sizes of the directories above can be found as follows:
The total size of directory 'e' is 584 because it contains a single file 'i' of size 584 and no other directories.
The directory 'a' has total size 94853 because it contains files 'f' (size 29116),
'g' (size 2557), and 'h.lst' (size 62596), plus file 'i' indirectly ('a' contains 'e' which contains 'i').
Directory 'd' has total size 24933642.
As the outermost directory, '/' contains every file. Its total size is 48381165, the sum of the size of every file.

In the example above, the directories which has a total size of at most 100000 are a and e;
the sum of their total sizes is 95437 (94853 + 584).
(As in this example, this process can count files more than once!)

part 2:
The total size of file system is 70000000, and we need at least 30000000 unused space.
the total size of used space is the size of '/'.
we need to find 1 directory that, if deleted, would free the minimum but enough amount of space
so that'll be at least 30000000 unused space.
Output: the size of the directory that'll free the minimum amount of space
needed to give us a total of 30000000 unused space.

example: consider the example from part 1.
In the example above, the total size of the outermost directory (and thus the total amount of used space)
is 48381165; this means that the size of the unused space must currently be 21618835,
which isn't quite the 30000000 required.
Therefore, we require a directory with total size of at least 8381165 to be deleted.

To achieve this, we have the following options:

Delete directory 'e', which would increase unused space by 584.
Delete directory 'a', which would increase unused space by 94853.
Delete directory 'd', which would increase unused space by 24933642.
Delete directory '/', which would increase unused space by 48381165.
Directories 'e' and 'a' are both too small; deleting them would not free up enough space.
However, directories 'd' and '/' are both big enough!
Between these, we choose the smallest: d, increasing unused space by 24933642.
"""


class TreeNode:
    """
    presents a tree's node - aka directory
    """

    def __init__(self, data):
        """
        init directory/node 'ROOT'

        the files and dirs that are INSIDE the current will be stored in a dict called 'children'
        size is currently 0 since there nothing inside
        father is currently none since it's a 'root'

        :param data: the dir's name
        """
        self.data = data
        self.children = {}
        self.size = 0
        self.father = None

    def add_child(self, child):
        """
        adds a child to a given node

        makes the child's father be this current node and updates current node's size according
        to the new child's size and so on for all fathers until we finally update the root too.

        :param child: the data of child to add
        :type: either TreeNode (directory) or TreeLeaf (file)
        """
        child.father = self
        self.children[child.data] = child
        self.size += child.size
        fathers = self.father
        while fathers is not None:
            fathers.size += child.size
            fathers = fathers.father

    def scan_dirs(self, first=True):
        """
        scans a given tree for its directories only

        lists up all directories in a given tree and their sizes

        :param first: shows if it's the first time scan_dirs is called since it's recursive
        :return: a list of tuples, each tuple includes the dir's name and size
        :rtype: list
        """
        ret = []
        if first:
            ret += [(self.data, self.size)]
        ret += [(child, self.children[child].size) for child in self.children if type(self.children[child]) == TreeNode]
        for child in self.children:
            if type(self.children[child]) == TreeNode:
                ret += self.children[child].scan_dirs(False)
        return ret

    def __repr__(self, level=0):
        """
        prints the tree

        :param level: shows how deep we are in the tree (for indentation)
        :return: a tree diagram that shows our given tree
        :rtype: str
        """
        ret = "\t" * level + "-(dir) " + repr(self.data) + " = " + repr(self.size) + "\n"
        for child in self.children:
            ret += self.children[child].__repr__(level + 1)
        return ret


class TreeLeaf:
    """
    presents a tree's leaf - aka file
    """

    def __init__(self, data, size):
        """
        init file/leaf as a 'separate leaf'

        the files and dirs that are INSIDE the current will be stored in a dict called 'children'
        size is currently 0 since there nothing inside
        father is currently none since it's a 'separate leaf'.
        the father will be assigned by a node that'll use add_child to add the leaf

        :param data: the file's name
        :param size: the file's size
        """
        self.data = data
        self.size = size
        self.father = '~'

    def __repr__(self, level=0):
        """
        prints the leaf

        :param level: shows how deep the leaf is in the tree (for indentation)
        :return: the leaf's data and sizes' line in the tree diagram
        :rtype: str
        """
        return "\t" * level + repr(self.data) + " = " + repr(self.size) + "\n"


def part1():
    """
    takes care of part 1

    reads Day7Input.txt and finds out all directories with a total size of 100000 or less

    :return: the total size of all directories that has a total size of 100000 or less
    :rtype: int
    """

    with open("Day7Input.txt", 'r') as f:
        lines = f.read().splitlines()
    # initiating the directories tree
    root = TreeNode("/")
    # assigning pointer to current directory
    pointer = root
    # we start scanning all commands after the first which was '$ cd /'
    for line in lines[1:]:
        # case: command
        if line.startswith('$'):
            # command: change directory
            if line[2:4] == 'cd':
                # '$ cd ..':  move out 1 level
                if line[5:] == '..':
                    pointer = pointer.father
                # '$ cd <dir_name>': move in 1 level into dir_name
                else:
                    pointer = pointer.children[line[5:]]
        # case: a line from ls printing
        else:
            # pointer contains a directory
            if line.startswith("dir "):
                # we add a new TreeNode to the pointer's children
                pointer.add_child(TreeNode(line[4:]))
            # pointer contains a file which means the line's format is '{number} {file_name}'
            else:
                file_data = line.split(' ')
                pointer.add_child(TreeLeaf(file_data[1], eval(file_data[0])))
    # print(root)
    # print(root.scan_dirs())
    print(sum(d[1] for d in root.scan_dirs() if d[1] <= 100000))


def part2():
    """
    takes care of part 2

    reads Day7Input.txt and finds out the directory with the smallest size that is still enough
    to free up enough space in the system if deleted, up to the total of 30000000 unused space

    :return: the size of the directory that'll free the minimum amount of space
    needed to give us a total of 30000000 unused space in the whole system.
    :rtype: int
    """
    with open("Day7Input.txt", 'r') as f:
        lines = f.read().splitlines()
    # initiating the directories tree
    root = TreeNode("/")
    # assigning pointer to current directory
    pointer = root
    # we start scanning all commands after the first which was '$ cd /'
    for line in lines[1:]:
        # case: command
        if line.startswith('$'):
            # command: change directory
            if line[2:4] == 'cd':
                # '$ cd ..':  move out 1 level
                if line[5:] == '..':
                    pointer = pointer.father
                # '$ cd <dir_name>': move in 1 level into dir_name
                else:
                    pointer = pointer.children[line[5:]]
        # case: a line from ls printing
        else:
            # pointer contains a directory
            if line.startswith("dir "):
                # we add a new TreeNode to the pointer's children
                pointer.add_child(TreeNode(line[4:]))
            # pointer contains a file which means the line's format is '{number} {file_name}'
            else:
                file_data = line.split(' ')
                pointer.add_child(TreeLeaf(file_data[1], eval(file_data[0])))
    free_space = 70000000 - root.size
    print(min(d[1] for d in root.scan_dirs() if d[1] + free_space >= 30000000))


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
