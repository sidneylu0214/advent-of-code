input_pairs = []
with open('input.txt', 'r') as input_file:
    for line in input_file:
        input_pairs.append(line[:-1].split(' | '))
    pass

def Encoder(input):
    inputs = sorted([set(i) for i in input.split(' ')], key=len)
    
    #  mmmm 
    # n    o
    # n    o
    #  pppp 
    # q    r
    # q    r
    #  ssss      

    # m is get by 7 - 1
    m = inputs[1] - inputs[0]
    set_or = inputs[0]

    # p_s is (2 and 3 and 5) - m
    set_mps = set.intersection(inputs[3], inputs[4], inputs[5])
    set_ps = set_mps - m

    # n is get by 4 - 1 - ps
    n = inputs[2] - inputs[0] - set_ps

    # q is 8 - 4 - mps
    q = inputs[9] - inputs[2] - set_mps

    # s is ps - 4
    s = set_ps - inputs[2]
    p = set_ps - s

    # 3 has set_or but 2 only has o
    list_235 = [inputs[3], inputs[4], inputs[5]]
    list_25 = [item - set_mps - n for item in list_235 if not (item >= set_or)]

    # 2 contain oq
    # 5 contain nr
    r = [x for x in list_25 if len(x) == 1][0]    
    o = set_or - r

    set_0 = inputs[9] - p
    set_1 = set_or
    set_2 = set().union(set_mps, o, q)
    set_3 = set().union(set_mps, set_or)
    set_4 = inputs[2]
    set_5 = inputs[9] - o - q
    set_6 = inputs[9] - o
    set_7 = inputs[1]
    set_8 = inputs[9]
    set_9 = inputs[9] - q    

    return [set_0, set_1, set_2, set_3, set_4, set_5, set_6, set_7, set_8, set_9]


def Decoder(table, messages):
    messages = [set(i) for i in messages.split(' ')]

    output = []
    for m in messages:
        output += [idx for idx, element in enumerate(table) if element == m]

    return output

# part 1
messages = []
for unencode_table, undecode_messages in input_pairs:
    encode_table = Encoder(unencode_table)
    messages += Decoder(encode_table, undecode_messages)
    
a = messages.count(1)
b = messages.count(4)
c = messages.count(7)
d = messages.count(8)
print(a+b+d+c)


# part 2
messages = []
for unencode_table, undecode_messages in input_pairs:
    encode_table = Encoder(unencode_table)
    decode_message = Decoder(encode_table, undecode_messages)
    d = decode_message
    messages.append(1000 * d[0] + 100 * d[1] + 10 * d[2] + 1 * d[3])

print(sum(messages))
