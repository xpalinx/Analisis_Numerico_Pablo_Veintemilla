import numpy as np
import matplotlib.pyplot as plt

acum = 0
cont = 0
conti = []
for n in range(2, 22):
    print(n, " => ", n**2)
    for i in range(n**2):
        acum += i**2
        cont += 1
    print(acum)
    conti.append(cont)
    cont = 0

x = np.linspace(1, 20, num=20)
y = conti
plt.suptitle('O(2**2)')
plt.xlabel('n')
plt.ylabel('operaciones')
plt.plot(x,y)
plt.show()
