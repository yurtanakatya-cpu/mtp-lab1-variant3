"""Простая точка входа для практики с Git."""

import sys

from greeting import greet


if __name__ == "__main__":
    name = "world" if len(sys.argv) == 1 else " ".join(sys.argv[1:])
    print(greet(name))
