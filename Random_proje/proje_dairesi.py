import random as rd 
import matplotlib.pyplot as plt

projelerD = open("C:/Users/ilbey/OneDrive/Masaüstü/Python/Projeler.txt", "r", encoding= "utf-8")


projeler= []
dilim=[]
sAyırma=[]
for satir in projelerD:
    projeler.append(satir)
    dilim.append(1)
    if (len(projeler)!=1):
        sAyırma.append(0)

r = rd.choice(projeler)
indexD= projeler.index(r)
print (r)


sAyırma.insert(indexD,0.1)

plt.pie(dilim, labels= projeler,radius=1.2, explode=sAyırma)
plt.show()