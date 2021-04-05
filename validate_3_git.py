def v(x):
    a, b, c = True, True, 0
    for i in range(len(x)): a = a and x[i] in "-1234567890."
    for j in range(1, len(x)): b = b and not (x[j] == "-")
    for k in range(len(x)): 
        if x[k] == ".": c+=1
    return a and b and c < 2

print(v('2.3'))
print(v('2..'))