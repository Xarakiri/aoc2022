import re
is_stack_input = True
stack_len = 0
stack = []
correct_stacks = []
pattern = re.compile(r'\d+')

with open('input', 'r') as f:
    for l in f.readlines():
        if stack_len == 0 and is_stack_input:
            stack_len = len(l.rstrip('\n'))

        if l[0] == " ": # stacks numbers line
            is_stack_input = False
            # transpose matrix, drop None`s
            correct_stacks = [[stack[j][i] for j in range(len(stack)-1, -1, -1) if stack[j][i] != None] for i in range(len(stack[0]))]
            continue
        if l == "\n":
            continue

        if is_stack_input:
            l = l.rstrip('\n')
            line = []
            for i in range(0, stack_len, 4):
                if l[i] != ' ':
                    line.append(l[i+1])
                else:
                    line.append(None)
            stack.append(line)
        else:
            count, from_, to = map(int, pattern.findall(l.strip()))
            while count:
                correct_stacks[to - 1].append(correct_stacks[from_ - 1].pop())
                count -= 1

s = ""
for l in correct_stacks:
    s += l[-1]

print(s)
