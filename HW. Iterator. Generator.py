nested_list = [['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],]

class FlatIterator:

    def __init__(self, some_list):
        self.some_list = some_list

    def __iter__(self):
        self.iter_list = iter(self.some_list)
        self.nested_list = []
        self.cursor = -1
        return self

    def __next__(self):
        self.cursor += 1
        if len(self.nested_list) == self.cursor:
            self.nested_list = None
            self.cursor = 0
            while not self.nested_list:
                self.nested_list = next(self.iter_list)
        return self.nested_list[self.cursor]

for item in FlatIterator(nested_list):
    print(item)

print()

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list, '\n')

def flat_generator(some_list):
    for sub_list in some_list:
        for el in sub_list:
            yield el

for item in  flat_generator(nested_list):
    print(item)
