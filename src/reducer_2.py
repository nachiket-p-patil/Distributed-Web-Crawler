import sys
for line in sys.stdin:
    line = line.strip().split()
    if line[1] in {'0', '1'}:
        print(*line)
    else:
        print(line[0], 1)