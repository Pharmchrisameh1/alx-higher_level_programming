#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """Create a locked class.

    Prevent the user from instantiating new LockedClass attributes
    for anything but attributes called 'first_name'.

    """

    __slots__ = ["first_name"]
