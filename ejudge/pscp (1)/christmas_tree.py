"""Chrismas Tree"""


def leaf_maker(leaf_size):
    """Make the leaf of the tree"""
    for i in range(1, leaf_size + 1):
        for _ in range(leaf_size - i):
            print(" ", end="")
        for _ in range(1, i + 1):
            print("*", end="")
        for _ in range(i - 1, 0, -1):
            print("*", end="")
        print()


def log_maker(leaf_size, body_size):
    """Make the body of the tree"""
    space_range = (leaf_size * 2) - 1
    for _ in range(body_size):
        print(" " * (int(space_range / 2) - 1) + "---")


def tree_maker(leaf_size, body_size):
    """Make a Chrismas tree"""
    leaf_maker(leaf_size)
    log_maker(leaf_size, body_size)


tree_maker(int(input()), int(input()))
