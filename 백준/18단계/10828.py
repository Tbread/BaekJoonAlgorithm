import sys
repeat = int(input())
stack = []
for rp in range(repeat):
    order = list(sys.stdin.readline().strip().split(' '))
    if order[0] == 'push':
        stack.append(order[1])
    elif order[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            temp_value = stack[-1]
            stack.pop()
            print(temp_value)
    elif order[0] == 'size':
        print(len(stack))
    elif order[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])