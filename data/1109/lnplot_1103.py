import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 24})
##f1=open("hgswp_1110_0.725_1.txt","r")
##f2=open("hgswp_1110_1.45_1.txt","r")
##f3=open("hgswp_1110_2.9_1.txt","r")

f1=open("hgswp_1110_0.6_2.txt","r")
f2=open("hgswp_1110_1.2_2.txt","r")
f3=open("hgswp_1110_2.4_2.txt","r")
x1a=[]
y1a=[]
x2a=[]
y2a=[]
x3a=[]
y3a=[]
for i in range(5):
    r=f1.readline()
    x,y,sp,sn=r.split()
    print(str(i)+" "+x+" "+y)
    x1a.append(float(x))
    y1a.append(float(y))
    
    r=f2.readline()
    x,y,sp,sn=r.split()
    print(str(i)+" "+x+" "+y)
    x2a.append(float(x))
    y2a.append(float(y))
    
    r=f3.readline()
    x,y,sp,sn=r.split()
    print(str(i)+" "+x+" "+y)
    x3a.append(float(x))
    y3a.append(float(y))


plt.plot(x1a,y1a,'o-',label="fg=0.5fg_max")
plt.plot(x2a,y2a,'o-',label="fg=1fg_max")
plt.plot(x3a,y3a,'o-',label="fg=2fg_max")

plt.legend()

plt.xlabel("frac_power")
plt.ylabel('Error')
plt.xscale('log')
plt.yscale('log')
plt.title("1-photon, t=2π/Ω")
plt.show()

