import math
import numpy as np
import time as time
import matplotlib.pyplot as plt
delay = 0.5
filename = 'date.in'
P = []

with open(filename) as f:
    "citesc n"
    punct = f.readline().split()
    n = int(punct[0])
    "citesc n puncte din infasuratoare"
    for i in range(0,n,1):
        punct = f.readline().split()
        punct[0] = float(punct[0])
        punct[1] = float(punct[1])
        "desenez punct negru"
        plt.plot(punct[0], punct[1], 'o', color='black')
        P.append(punct)

    "citesc punctul pe care trebuie sa-l adaug la infasuratoare si il desenez albastru"
    punct = f.readline().split()
    punct[0] = float(punct[0])
    punct[1] = float(punct[1])
    plt.plot(punct[0], punct[1], 'o', color='violet')
    plt.draw()
    plt.pause(delay)


"desenez cele n linii le fac rosii"
P.append(P[0])
for i in range(2,n+2,1):
    plt.plot([P[i-2][0],P[i-1][0]],[P[i-2][1],P[i-1][1]], 'r--')
    plt.draw()
    plt.pause(delay)

"sterg primul punct din lista si il adaug la lista de puncte pe cel nou citit"
P.remove(P[n])
P.append(punct)

def unghi(O,A,B):
    return (A[0]-O[0])*(B[1]-O[1])-(A[1]-O[1])*(B[0]-O[0])

def comp(A,B):
    return unghi(punct,A,B)<0

ind=0
for i in range(0,n+1,1):
    if(P[i]<P[ind]):
        ind=i

punct = P[ind]
P.remove(P[ind])
"sortez vectorul"
for i in range(0,n-1,1):
    for j in range(i+1,n,1):
        if(comp(P[i],P[j])==0):
            aux=P[i]
            P[i]=P[j]
            P[j]=aux
"fac stiva cu convexa"
stiva = []
stiva.append(punct)
stiva.append(P[0])
k = 1
for i in range(1,n,1):
    while k>=1 and unghi(stiva[k-1],stiva[k],P[i])>0 :
        stiva.remove(stiva[k])
        k=k-1
    stiva.append(P[i])
    k=k+1
"desenez convexa"
stiva.append(stiva[0])
k=k+1
for i in range(2,k+2,1):
    plt.plot([stiva[i-2][0],stiva[i-1][0]],[stiva[i-2][1],stiva[i-1][1]], 'b-')
    plt.draw()
    plt.pause(delay)
"afisez convexa"
stiva.reverse()
for i in range(0,k+1,1):
    print(stiva[i][0],stiva[i][1])
"dau remove la linii nedorite"
ax = plt.gca()
def removeLines():
    i = 0
    for line in ax.lines:
        lineData = line.get_data()
        remove1 = True
        remove2 = True
        if(len(lineData[0]) > 1):
            x1 = lineData[0][0]
            x2 = lineData[0][1]
            y1 = lineData[1][0]
            y2 = lineData[1][1]
            for item in stiva:
                if x1 == item[0] and y1 == item[1]:
                    remove1 = False
                if x2 == item[0] and y2 == item[1]:
                    remove2 = False

            if remove1 == True or remove2 == True:
                line.remove()
                i = 1
    return i

ok = 1
while ok==1:
    ok = removeLines()
plt.show()
