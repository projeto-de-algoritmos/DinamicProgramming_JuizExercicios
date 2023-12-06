def groupThePeople(groupSizes):
    groups = {}
    result = []

    for i, size in enumerate(groupSizes):
        if size not in groups:
            groups[size] = [i]
        else:
            groups[size].append(i)

        if len(groups[size]) == size:
            result.append(groups[size])
            groups[size] = []

    return result

# Exemplo 1
input1 = [3, 3, 3, 3, 3, 1, 3]
output1 = groupThePeople(input1)
print(output1)

# Exemplo 2
input2 = [2, 1, 3, 3, 3, 2]
output2 = groupThePeople(input2)
print(output2)
