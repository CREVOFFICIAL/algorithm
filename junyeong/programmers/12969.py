rows, columns = map(int, input().strip().split(' '))
for column in range(columns):
    for row in range(rows):
        print("*", end='')
    print("\n", end='')
