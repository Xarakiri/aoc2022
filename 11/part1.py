import copy
from math import floor
from typing import List


class Monkey:
    def __init__(self, items: List[int], op: str, op_v1: str, op_v2: str, test_v: int, test: List[int]):
        self.items = items
        self.op = op
        self.op_v1 = op_v1
        self.op_v2 = op_v2
        self.test_v = test_v
        self.test = test
        self.inspected = 0

    def __repr__(self):
        return f"Starting items: {self.items}\n" + \
            f"Operation: new = {self.op_v1} {self.op} {self.op_v2}\n" + \
            f"Test: divisible by {self.test_v}\n" + \
            f"   If true: throw to monkey {self.test[0]}\n" + \
            f"   If false: throw to monkey {self.test[1]}\n"


monkeys = []
with open('./input', 'r') as f:
    lines = list(map(lambda x: x.rstrip('\n'), f.readlines()))
    i = 0
    while i < len(lines):
        if 'Monkey' in lines[i]:
            i += 1
            items = list(map(int, lines[i].split(":")[1].split(",")))
            i += 1
            ops = lines[i].split("=")[1].split()
            op_v1, op, op_v2 = ops
            i += 1
            test = int(lines[i].split()[-1])
            i += 1
            test_true = int(lines[i].split()[-1])
            i += 1
            test_false = int(lines[i].split()[-1])
            i += 1
            monkey = Monkey(items, op, op_v1, op_v2, test, [test_true, test_false])
            monkeys.append(monkey)
        else:
            i += 1

# Супер-модуль — наименьшее общее кратное
# Если супер-модуль, например, 2*3*5 = 30,
# уровень переживания, например, 35,
# то результат проверки на кратность на 2, 3, 5
# для 35 % 30 = 5 такой же, как и для 35:
# 35 % 2 = 1    5 % 2 = 1
# 35 % 3 = 2    5 % 3 = 2
# 35 % 5 = 0    5 % 5 = 0

super_mod = 1
for m in monkeys:
    super_mod *= m.test_v


def solve(rounds, monkeys, is_part2=False):
    while rounds:
        for monkey in monkeys:
            while monkey.items:
                item = monkey.items.pop()
                item = item % super_mod  # избавляемся от слишком большого числа, если такое получилось
                op1 = item
                if monkey.op_v2 == 'old':
                    op2 = item
                else:
                    op2 = int(monkey.op_v2)
                if monkey.op == '*':
                    worry_level = op1 * op2
                else:
                    worry_level = op1 + op2

                if not is_part2:
                    worry_level = floor(worry_level / 3)

                if worry_level % monkey.test_v == 0:
                    monkeys[monkey.test[0]].items.append(worry_level)
                else:
                    monkeys[monkey.test[1]].items.append(worry_level)
                monkey.inspected += 1
        rounds -= 1
    most_inspected = list(sorted(monkeys, key=lambda x: x.inspected, reverse=True))
    return most_inspected[0].inspected * most_inspected[1].inspected


print('part 1 = ', solve(20, copy.deepcopy(monkeys)))
print('part 2 = ', solve(10000, copy.deepcopy(monkeys), True))
