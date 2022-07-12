import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 16})
plt.rcParams["figure.figsize"] = (3.375,3.375)

tpi=2
f=open("fmaxswp_0118_2.txt","r")
xa=[]
y1a=[]
y2a=[]
for i in range(80):
    r=f.readline()
    x,y1,y2,sn,sp=r.split()
    print(str(i)+" "+x+" "+y1+" "+y2)
    xa.append(float(x))
    y1a.append(float(y1))
    y2a.append(float(y2))


plt.plot(xa,y1a,'o-',label="Numerics",color='red')
plt.plot(xa,y2a,'-',label="Theory",color='blue')
plt.legend(loc="lower right", prop={'size': 12})
plt.xlabel("Bandwidth/(Ω0/2π))")
plt.ylabel('Error')
plt.yscale('log')

filestr='fmaxswp_'+str(tpi)+'pi.png'
plt.savefig(filestr, bbox_inches='tight',dpi=100)
