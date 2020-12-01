import matplotlib.pyplot as plt

beta = 0.185
alpha = 0.0132
nP = 50865708

fs = lambda s,i: -beta*s*i/nP
fi = lambda s,i: -fs(s,i) - alpha*i
fr = lambda i: alpha*i

i = [72,144]
r = [0,2]
s = [nP - i[0] + r[0],nP - i[1] + r[1]]

for k in range(252):
    s.append(s[-1] + fs(s[-1],i[-1]))
    i.append(i[-1] + fi(s[-2],i[-1]))
    r.append(r[-1] + fr(i[-2]))

for k in range(len(s)):
    print("Dia ",k + 1,"-> [{:.5f},{:.5f},{:.5f}]".format(s[k],i[k],r[k]))

plt.plot(range(len(s)),s,"r")
plt.plot(range(len(i)),i,"b")
plt.plot(range(len(r)),r,"g")
plt.show()