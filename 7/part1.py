import typing


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __repr__(self):
        return f"({self.name}, {self.size})"


class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.child = []
        self.files: typing.List[File] = []

    @property
    def size(self) -> int:
        return sum([i.size for i in self.files]) + sum([i.size for i in self.child])

    def __repr__(self):
        return f"({self.name}, {self.size})"


class FileSystem:
    def __init__(self):
        self.root = Directory("/")

    def restore(self, lines: typing.List[str]):
        currentDir = self.root

        for l in lines:
            parts = l.split(' ')
            if parts[0] == "$":
                if parts[1] == "cd":
                    if parts[2] == "/":
                        currentDir = self.root
                    elif parts[2] == "..":
                        currentDir = currentDir.parent
                    else:
                        for i in currentDir.child:
                            if i.name == parts[2]:
                                currentDir = i
            elif parts[0] == "dir":
                currentDir.child.append(Directory(parts[1], currentDir))
            else:
                currentDir.files.append(File(parts[1], int(parts[0])))

    def flatten(self):
        q = []
        q.extend(self.root.child)
        answer = [self.root]

        # BFS
        while len(q) > 0:
            s = len(q)
            while s > 0:
                s -= 1
                curr = q.pop(0)

                if curr is None:
                    continue
                answer.append(curr)

                q.extend(curr.child)
        return answer


f = FileSystem()
f.restore([x.rstrip('\n') for x in open('./input').readlines()])

flat = f.flatten()
print('part 1 =', sum([i.size for i in flat if i.size < 100_000]))

needSpace = 30_000_000 - (70_000_000 - max([i.size for i in flat]))
print('part 2 = ', min([i.size for i in flat if i.size > needSpace]))
