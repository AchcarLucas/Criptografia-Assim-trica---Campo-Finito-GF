import math
import numpy as np

def inverse(r, p):
    t = 1

    aux = int(p)
    newr = int(r)
    newt = math.ceil(0 - (aux / r))

    while(True):
        r = newr
        newr = aux % r

        if newr is 0:
            break

        aux = t
        t = newt
        newt = aux - t * math.floor(r / newr)
        aux = r

    t = round(t)

    if (t < 0):
        return t + p
    
    return t

p = 47

c_x = range(1, p)
c_y = range(1, p)

print("      ", end = " ")
for y in c_y:
    print(f"{y:03d}  ", end=" ")

print("\n")
print("=" * 85)

table_inverse = np.zeros((p - 1, p - 1))

for x in c_x:
    print(f" {x:03d} | ", end="")
    for y in c_y:
        mod = ((x * y) % p)
        print(f"{mod:{3:03d}}  ", end = " ")
        table_inverse[x - 1][y - 1] = mod
    print(end="\n")

inv = 44
print(f"Inverso do nº {inv} é {inverse(inv, p)}")

y = 1
for value in table_inverse[inv - 1]:
    if value == 1:
        print(f"Inverso table : {y}")
    y += 1
