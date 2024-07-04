#!/usr/bin/python3
"""
Lockboxes Problem

This script contains a method to determine if all the boxes in a
given list of lists can be unlocked.
Each box is numbered sequentially from 0 to n - 1 and may contain
keys to other boxes. The goal is to check if all boxes can be opened
starting from the first box, which is initially unlocked.

"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Parameters:
    boxes (list of lists): List where each element is a list of
    keys contained in that box.

    Returns:
    bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes:
        return False

    n = len(boxes)
    unlocked = set([0])  # Start with the first box unlocked
    keys = set(boxes[0])  # Start with the keys from the first box

    while keys:
        new_keys = set()
        for key in keys:
            # If the key is valid and the box is not yet unlocked
            if key < n and key not in unlocked:
                new_keys.update(boxes[key])
        keys = new_keys

    return len(unlocked) == n
