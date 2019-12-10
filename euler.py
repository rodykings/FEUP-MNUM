
h = 0.25

def dydt(z):
    return z

def dzdt(t, z):
    return 2+t**2+t*z

#2, 0.25, 1, 1, 0
def euler(a, h, t0, y0, dy, n):
    y = y0
    z = dy
    t = t0
    for i in range(n):
        dz = h * dzdt(t, z)
        dy = h * dydt(z)
        z+=dz
        y+=dy
        t+=h
    return [t, y]

print(euler(2, 0.25, 1.0, 1.0, 0, 0))
print(euler(2, 0.25, 1.0, 1.0, 0, 1))
print(euler(2, 0.25, 1.0, 1.0, 0, 2))
    
    
    


    