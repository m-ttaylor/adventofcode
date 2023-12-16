from collections import defaultdict
from dataclasses import dataclass
from functools import cache
import sys
from utils import aoc

from enum import Enum

# import numpy as np
from numpy import array

sys.setrecursionlimit(4000)
TEST = False

data = aoc.getInput(2023, 16, TEST)

contraption = array([list(line) for line in data])

NORTH, EAST, SOUTH, WEST = (0, -1), (1, 0), (0, 1), (-1, 0)  # x, y vectors

w, h = contraption.shape

# NUMPY IS ROW, COLUMN ACCESS
print(contraption.shape)

lit = set()

lightSymbol = {NORTH: "^", EAST: ">", SOUTH: "v", WEST: "<"}


memo = set()


def emit(sx, sy, dir):
    dx, dy = dir

    def inBounds(x, y):
        return 0 <= x + dx < w and 0 <= y + dy < h

    if inBounds(sx, sy):
        nx, ny = sx + dx, sy + dy

        if ((ny, nx), dir) in memo:
            return

        memo.add(((ny, nx), dir))
        lit.add((ny, nx))

        if contraption[ny, nx] not in {"|", "-", "\\", "/"}:
            contraption[ny, nx] = lightSymbol[dir]

        match contraption[ny, nx]:
            case "|":
                if dir in (EAST, WEST):
                    emit(nx, ny, NORTH)
                    emit(nx, ny, SOUTH)
                else:
                    emit(nx, ny, dir)
            case "\\":
                if dir == NORTH:
                    emit(nx, ny, WEST)
                elif dir == EAST:
                    emit(nx, ny, SOUTH)
                elif dir == SOUTH:
                    emit(nx, ny, EAST)
                elif dir == WEST:
                    emit(nx, ny, NORTH)
            case "/":
                if dir == NORTH:
                    emit(nx, ny, EAST)
                elif dir == EAST:
                    emit(nx, ny, NORTH)
                elif dir == SOUTH:
                    emit(nx, ny, WEST)
                elif dir == WEST:
                    emit(nx, ny, SOUTH)
            case "-":
                if dir in (NORTH, SOUTH):
                    emit(nx, ny, EAST)
                    emit(nx, ny, WEST)
                else:
                    emit(nx, ny, dir)
            case _:
                emit(nx, ny, dir)


emit(-1, 0, EAST)
print(len(lit))
print(contraption)


def part1():
    pass


def part2():
    pass


print(part1())
print(part2())
