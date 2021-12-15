from aoc import aoc

OPEN = {'(': ')', '<': '>', '{': '}', '[': ']'}
CLOSE = {')': '(', '>': '<', '}': '{', ']': '['}
SCORE = {')': 3, '>': 25137, '}': 1197, ']': 57}
SCORE2 = {')': 1, '>': 4, '}': 3, ']': 2}


def func():
    return None

ans, ans2 = 0, []

input = aoc.read_input('../input/in.txt')
for line in input:
    stack = []
    f = True
    for ch in line.strip():
        if ch in OPEN:
            stack.append(ch)
        elif ch in CLOSE and stack[-1] == CLOSE[ch]:
            stack.pop()
        else:
            aoc.logger(f"Expected {CLOSE[ch]}, but found {ch} instead.")
            ans += SCORE[ch]
            f = False
            break
    if f:
        total = 0
        while stack:
            x = OPEN[stack.pop()]
            total = total * 5 + SCORE2[x]
        ans2.append(total)

print(ans)

print(sorted(ans2)[len(ans2)//2])