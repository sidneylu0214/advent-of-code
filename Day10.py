import bisect

input_pairs = []
with open('input.txt', 'r') as input_file:
    for line in input_file:
        input_pairs.append(line[:-1])
    pass

# part 1
class Stack:
    def __init__(self):
        self.stack = []
    
    def PushBack(self, item):
        self.stack.append(item)
    
    def Pop(self):
        return self.stack.pop()
       
    def NotEmpty(self):
        return bool(len(self.stack))
    pass


corrupted = []
incomplete = []
value_1 = {')': 3, ']': 57, '}': 1197, '>': 25137}
value_2 = {'(': 1, '[': 2, '{': 3, '<': 4}
brackets = ['|', ')', ']', '}', '>']

for input in input_pairs:
    stack = Stack()
    is_corrupted = False

    for i in input:
        if i in value_2:
            stack.PushBack(value_2[i])
        else :
            if i != brackets[stack.Pop()]:
                is_corrupted = True
                corrupted.append(value_1[i])
                break

    if (not is_corrupted) and stack.NotEmpty() :
        incomplete.append(stack.stack)
    pass

# part 1
print(sum(corrupted))

# part 2
results = []
for output in incomplete:   
    bisect.insort(results, sum([output[i] * 5 ** i for i in range(len(output))]))

print(results[len(results) // 2])
