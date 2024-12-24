from collections import defaultdict, Counter
from functools import reduce
from heapq import heappop, heappush

from utils import aoc

fourDirs = ((1, 0), (0, 1), (-1, 0), (0, -1))  # up right down left

YEAR = 2024
DAY = 17
TEST = False

file = f"{YEAR}/{DAY}/test.txt" if TEST else f"{YEAR}/{DAY}/input"

with open(file) as f:
    data = f.read().strip().split("\n")

registers = data[:3]
rest = data[4:]

A = int(registers[0].split("A: ")[1])
B = int(registers[1].split("B: ")[1])
C = int(registers[2].split("C: ")[1])
str_program=rest[0].split("Program: ")[1]
program = aoc.parseInts(rest[0].split("Program: ")[1])


print(A, B, C)
print(program)


def eval(A, B, C, ip=0, rtn = [], pt2=False):
    rtn = []
    while ip in range(len(program)):
        combo = {0:0, 1:1, 2:2, 3:3, 4: A, 5: B, 6: C}
      
        match program[ip:ip+2]:
            case 0, op: A = A >> combo[op]
            case 1, op: B = B ^ op
            case 2, op: B = combo[op] % 8
            case 3, op: ip = op-2 if A else ip
            case 4, op: B = B ^ C
            case 5, op: 
                rtn.append(str(combo[op] % 8))
                if pt2 and rtn[len(rtn)-1] != program[len(rtn)-1]:
                    return rtn
            case 6, op: B = A >> combo[op]
            case 7, op: C = A >> combo[op]
        ip += 2
    return rtn
    
print(",".join(eval(A, B, C)))

target = "2,4,1,1,7,5,1,5,4,3,5,5,0,3,3,0"
# program = list(map(str, program))

# for p in program:
#     print(p)

print("program is:", "\n"+",".join(map(str, program)))
print(len(program))
program2 = list(map(str, program))
print(program2)
out = eval(1, 0, 0)
print(out)
# 2411751543550330
# for i in range(35_185_000_000_000, 100_000_000_000_000, 1_000_000_000):
# for i in range(100_000_000_000_000, 300_000_000_000_000, 10_000_000_000):
#     out = eval(i, 0, 0)
#     n = len(out)

#     if n == len(program) and out[-1] == program2[-1]:
#         print("match", i)
#         print(",".join(out))
#     # if n == len(program):
#     #     print("match", i)
#         # break
#     # if prev > n:
#     #     print(f"inflection at {i=}")
#     # print(",".join(out))
#     # ",".join(eval(i, B, C))
#     # prev = n
a = 0
# best = 0
# while True:
#     a += 1
#     #A = Ast * 8**5 + 0o36017
#     A = a * 8**9 + 0o676236017
#     out = eval(A, 0, 0, True)
#     if out == program:
#         print(A)
#         break
#     elif len(out) > best:
#         #print(A, oct(A), best, len(program))
#         best = len(out)


g = list( map( int, open( "2024/17/input" ).read().split()[ -1 ].split( ',' ) ) )

def solve( p, r ):
    if p < 0:
        print( r )
        return True
    for d in range( 8 ):
        a, i = r << 3 | d, 0
        while i < len( g ):
            if   g[ i + 1 ] <= 3: o = g[ i + 1 ]
            elif g[ i + 1 ] == 4: o = a
            elif g[ i + 1 ] == 5: o = b
            elif g[ i + 1 ] == 6: o = c
            if   g[ i ] == 0: a >>= o
            elif g[ i ] == 1: b  ^= g[ i + 1 ]
            elif g[ i ] == 2: b   = o & 7
            elif g[ i ] == 3: i   = g[ i + 1 ] - 2 if a != 0 else i
            elif g[ i ] == 4: b  ^= c
            elif g[ i ] == 5: w   = o & 7; break
            elif g[ i ] == 6: b   = a >> o
            elif g[ i ] == 7: c   = a >> o
            i += 2
        if w == g[ p ] and solve( p - 1, r << 3 | d ):
            return True
    return False

solve( len( g ) - 1, 0 )
