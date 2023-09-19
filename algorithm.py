import math

p = 47

A = 22
B = 15

def curve(x, y, A, B):
    return (y ** 2) % p == ((x ** 3) + (A * x) + B) % p

def modp(n, p):
        n = n % p
        if n < 0:
            return p + n

        return n

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

def calc_m(x1, y1, x2, y2, A, p):
    if(x1 is x2 and y1 is y2):
        return modp(((inverse(y1 * 2, p)) * ((x1 * 3) * x1 + A)), p)
    return modp((y2 - y1) * inverse(modp(x2 - x1, p), p), p);

def calc_x3_y3(x1, y1, x2, m):
    x3 = modp((m ** 2) - x1 - x2, p)
    y3 = modp(-(modp(m * (x3 - x1), p) + y1), p)
    return {'x': x3, 'y': y3}

c_x = range(0, p - 1)
c_y = range(0, p - 1)

points = []

for _x in c_x:
    for _y in c_y:
        if curve(_x, _y, A, B):
            print(f"({_x}, {_y})")
            points.append({'x': _x, 'y': _y})

print("=" * 30)
print(f"Achou: {len(points)} pontos na curva")
print("=" * 30)
print(f"Inicio do ponto ({points[0]})")
print("=" * 30)

x1 = points[0]['x']
y1 = points[0]['y']

# primeira iteração do 'n'
m = calc_m(x1, y1, x1, y1, A, p)
print(f'm: {m}')

# x2 = x1 na primeira iteração
x3_y3 = calc_x3_y3(x1, y1, x1, m)
print(x3_y3)

find_points = []

find_points.append({'x': x1, 'y': y1})

for i in range(1, len(points) - 1):
    m = calc_m(x1, y1, x3_y3['x'], x3_y3['y'], A, p)
    print(f'm: {m}')

    x2 = x3_y3['x']
    y2 = x3_y3['y']

    x3_y3 = calc_x3_y3(x1, y1, x2, m)

    find_points.append(x3_y3)

    x1 = x2
    y1 = y2

    if(x1 == points[0]['x'] and y1 == points[0]['y']):
        # adiciona +2 pois antes do loop já encontramos 2 pontos
        print(f"Voltou ao ponto em {i + 2} iterações")

    print(x3_y3)

check_point = True

for point in find_points:
    if point not in points:
        check_point = False

print("=" * 30)

if(check_point):
    print("Todos os pontos pertencem ao GF")
else:
    print("Existem pontos que não pertencem ao GF")
print("=" * 30)
    




