from scipy import matrix, rand
from time import perf_counter
tiempo = [[],[],[],[],[],[],[],[],[],[]]
nm = [1,4,10,11,13,15,20,30,40,45,50,55,60,75,80,100,130,170,200,240,345,500,600,800,100,2000,5000,10000]
for i in range(0,10):
    for N in nm:
        A = matrix(rand(N,N))
        B = matrix(rand(N,N))

        t1 = perf_counter()
        C = A*B
        t2 = perf_counter()

        dt = t2 - t1
        tiempo[i].append(dt)
print(tiempo)
