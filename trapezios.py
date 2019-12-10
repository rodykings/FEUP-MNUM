#duplo integral

m = [[1.1, 1.4, 7.7], [2.1, 3.1, 2.2],[7.3, 1.5, 1.2]]

h=1
fa = m[0][0]
fb = m[0][2]


trap0 = (h/2)*(fa + fb + 2*m[0][1])
trap1 = (h/2)*(m[1][0] + m[1][2] + 2*m[1][1])
trap2 = (h/2)*(m[2][0] + m[2][2] + 2*m[2][1])

trap = (h/2)*(trap0 + trap2 + 2*trap1)

print(trap)
        
        
        
        