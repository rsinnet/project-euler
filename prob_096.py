#!/usr/bin/python

# Project Euler
# Problem 96
# Su Doku

def same_row(i,j): return (i/9 == j/9)
def same_col(i,j): return (i-j) % 9 == 0
def same_block(i,j): return (i/27 == j/27 and i%9/3 == j%9/3)

glob_r = 0

def r(a):
    i = a.find('0')
    if i == -1:
        global glob_r
        glob_r = a
        return

    excluded_numbers = set()
    for j in range(81):
        if same_row(i,j) or same_col(i,j) or same_block(i,j):
            excluded_numbers.add(a[j])

    for m in '123456789':
        if m not in excluded_numbers:
            # At this point, m is not excluded by any row, column, or block,
            # so let's place it and recurse
            r(a[:i]+m+a[i+1:])

def solve_r(a):
    r(a)
    return glob_r

is_reading = False
current_puzzle = ''
cum_sum = 0
with open('sudoku.txt', 'rb') as file:
    for row in file:
        foo = row.strip()

        if is_reading:
            current_puzzle += foo
            if len(current_puzzle) >= 81:
                is_reading = False
                # solve puzzle
                print 'puz: ', current_puzzle
                foo = solve_r(current_puzzle)
                print 'sol: ', foo
                cum_sum += int(foo[:3])
                print

        if foo[:4] == 'Grid':
            is_reading = True
            current_puzzle = ''

print 'Sum of three-digit top-left numbers: {}'.format(cum_sum)
