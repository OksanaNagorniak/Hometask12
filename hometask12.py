n = int(input())
operations = {'write': 'W', 'read': 'R', 'execute':'X'}
file_names = {}
for i in range(n):
    a, *b = input().split()
    file_names[a] = set(b)
for i in range(int(input())):
    a, b = input().split()
    if operations[a] in file_names[b]:
        print("OK")
    else:
        print('Access denied')