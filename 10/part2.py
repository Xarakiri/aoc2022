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


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i: i + n]


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

# Пиксель нужно рисовать, только если значение регистра X на этом цикле
# отличается от X-позиции луча не более чем на 1.
for row in chunks(stack, 40):
    print(''.join(["#" if abs(vm[0] - ((vm[1] - 1) % 40)) <= 1 else " " for vm in row]))
