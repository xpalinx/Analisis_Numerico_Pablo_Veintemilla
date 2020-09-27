import numpy as np
import matplotlib.pyplot as plt
count = 0
bs = 0
bi = []
bc = 0
bci = []
print("para inferior presione i, para superor s")
option = input()
if(option == 's'):
    for n in range (2, 22):
        A = np.random.randn(n,n)
        for i in range(n):
            for j in range(n):
                if(j>=i):
                    count = count + A[i][j]
                    bs += 1
        print(bs, "operaciones para n =" , n)
        print('Suma de matriz ', count)
        bi.append(bs)
        bs = 0
        print()
else:
    for n in range (2, 22):
        A = np.random.randn(n,n)
        for i in range(n):
            for j in range(n):
                if(j<=i):
                    count = count + A[i][j]
                    bs += 1
        print(bs, "operaciones para n =" , n)
        print('Suma de matriz ', count)
        bi.append(bs)
        bs = 0
        print()
x = np.linspace(1, 20, num=20)
y = bi
plt.suptitle('O(nlogn)')
plt.xlabel('n')
plt.ylabel('operaciones')
plt.plot(x,y)
plt.show()


