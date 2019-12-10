
l = [0.37, 0.38, 1.49, 1.08, 0.13, 0.64, 0.84]

h = 1
a = 0.00
b = 2.00
fa = 1.04
fb = 0.12



par = []
impar = []
result = [0, 0, 0]
i = a + h    

counter = 0
for r in range(0, 3):
    i = a+h
    while(i != b):
        if(counter % 2 == 0):
            par.append(l[counter])
        else:
            impar.append(l[counter])
        counter+=1
        i += h
    result[r] = (h/3) * (fa+fb+4*sum(par)+2*sum(impar))
    h /= 2
    par = []
    impar = []
    
    
    counter = 0

err = (result[2]-result[1])/15
    
print("res: ", result, " err: ", err)
    
    