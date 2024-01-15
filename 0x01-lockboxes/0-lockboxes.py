#!/usr/bin/python3
"""
 Lock boxes problem AFRICA Problem
"""

def canUnlockAll(boxes):
    """
    Lock boxes plobem solved
    """
    if (type(boxes) is not list):
        return False
    elif (len(boxes) == 0):
        return False
    for k in range(1, len(boxes) - 1):
        checked = False
        for idx in range(len(boxes)):
            checked = k in boxes[idx] and k != idx
            if checked:
                break
        if checked is False:
            return checked
    return True
