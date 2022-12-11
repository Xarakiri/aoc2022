class Signal:
    def __init__(self, input: str):
        params = input.split()
        self.type_ = params[0]

        if len(params) > 1:
            self.args = int(params[1])
        else:
            self.args = 0

    def __repr__(self):
        return f'{self.type_} {self.args}'


ops = [Signal(j) for j in [i.rstrip('\n') for i in open('./input').readlines()]]


def run(ops):
    cycle = 0
    x = 1
    for op in ops:
        if op.type_ == 'addx':
            cycle += 1
            yield [x, cycle]
            cycle += 1
            yield [x, cycle]
            x += op.args
        else:
            cycle += 1
            yield [x, cycle]


stack = list(run(ops))
strength = 0
for s in stack:
    if s[-1] in (20, 60, 100, 140, 180, 220):
        strength += s[0] * s[-1]
print('part 1 = ', strength)
