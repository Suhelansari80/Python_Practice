x = [1, 22, 33, 4, 22, 33]
y = []
for i in range(len(x)):
    for j in range(i + 1, len(x)):
        if x[i] == x[j] and j not in y:
            y.append(x[j])
print(y)
