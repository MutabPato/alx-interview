#!/usr/bin/python3
"""Lockboxes"""


def canUnlockAll(boxes):
    """Determines if all the boxes can be opened"""
    n = len(boxes)  # Number of boxes
    visited = [False] * n  # List to keep track of opened boxes
    visited[0] = True  # Start with box 0
    queue = [0]  # Starting with first box in queue

    while queue:
        current_box = queue.pop(0)  # Get next box to process

        # Check all the keys in the current box
        for key in boxes[current_box]:
            if key < n and not visited[key]:  # Only process valid boxes
                visited[key] = True  # Mark this as opened
                queue.append(key)  # Add box to stack to explore its keys

    return all(visited)  # Check if all boxes have been visited
