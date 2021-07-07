import matplotlib.pyplot as plt
print(3/5)
f=open("fswp_0706_1.txt","r")
xa=[]
ya=[]
for i in range(80):
    r=f.readline()
    x,y=r.split()
    print(str(i)+" "+x+" "+y)
    xa.append(float(x))
    ya.append(float(y))


plt.plot(xa,ya)
plt.xlabel("fcenter/(Ω0/2π))")
plt.ylabel('error')
plt.show()

