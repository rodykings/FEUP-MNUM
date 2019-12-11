#runge kuta de ordem 4

def dydt(t, y, z):
    return z

def dzdt(t, y, z):
    return 2+t**2+t*z


def rk_4(h, t0, y0, dy, n):
    
    t = t0
    y = y0
    z = dy
    
    for i in range(n):
        dy1 = h*dydt(t, y, z)
        dz1 = h*dzdt(t, y, z)
        
        dy2 = h*dydt(t+h/2, y+dy1/2, z+dz1/2)
        dz2 = h*dzdt(t+h/2, y+dy1/2, z+dz1/2)
        
        dy3 = h*dydt(t+h/2, y+dy2/2, z+dz2/2)
        dz3 = h*dzdt(t+h/2, y+dy2/2, z+dz2/2)
        
        dy4 = h*dydt(t+h, y+dy3, z+dz3)
        dz4 = h*dzdt(t+h, y+dy3, z+dz3)
        
        dy = dy1/6+dy2/3+dy3/3+dy4/6
        dz = dz1/6+dz2/3+dz3/3+dz4/6
        
        y+=dy
        z+=dz
        t+=h
        
    return [t, y, z]


print(rk_4(0.25, 1.0, 1.0, 0, 0))  
print(rk_4(0.25, 1.0, 1.0, 0, 1))  
print(rk_4(0.25, 1.0, 1.0, 0, 2))     
        
        
    
    
    

