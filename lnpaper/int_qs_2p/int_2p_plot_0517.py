import matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.rcParams.update({'font.size': 12})


plt.subplot(2,2,1)

h0=200

print(3/5)
tpi=1

filestr="intswp2_1.txt"
f=open(filestr,"r")
xa=[]
ya=[]
ta=[]
spa=[]
sna=[]
omegar=2*np.pi*(1e6)
h_g=200


for i in range(10):
    r=f.readline()
    x,y,sp,sn=r.split()
    print(str(i)+" "+x+" "+y)
    xa.append(0.01*(i+1))
    ya.append(float(y))
    spa.append(float(y)+float(sp))
    sna.append(float(y)-float(sn))
##    if(i==40):
##        x=1
    fg=float(x)*(1e6)

    #print(2*omegag**2*sg/(omegar**2))
    N=1/2
    et=N**2*(np.pi)**2*(0.02*(i+1))**2/4
    ta.append(1*et)


plt.plot(xa,ya,'o-',label="Numerics",color='red')
plt.plot(xa,ta,label="Theory",color='blue')
#plt.plot(xa,spa,'r',alpha=0.2,label="Uncertainty")
#plt.plot(xa,sna,'r',alpha=0.2)
#plt.fill_between(xa,spa,sna,color='crimson',alpha=0.1)
#plt.legend(loc="lower right", prop={'size': 10})
plt.yscale('log')
plt.text(0.01, 0.02, 'a', horizontalalignment='center',
     verticalalignment='center')

plt.xlabel("RIN")
plt.ylabel('Error')
f.close()


plt.subplot(2,2,2)
tpi=1
filestr="0508_2p_1w.txt"
f=open(filestr,"r")
xa=[]
ya=[]
ta=[]
spa=[]
sna=[]
omegar=2*np.pi*(1e6)
h_g=200
for i in range(8):
    rtmp=f.readline()
for i in range(10):
    r=f.readline()
    r=f.readline()
    r=f.readline()
    y=r.split()
    print("y="+str(y))
    xa.append(0.01*(i+1))
    ya.append(1-float(y[0]))
    spa.append(0)
    sna.append(0)
##    if(i==40):
##        x=1
    fg=float(x)*(1e6)

    #print(2*omegag**2*sg/(omegar**2))
    N=1/2
    et=N**2*(np.pi)**2*(0.02*(i+1))**2/4
    ta.append(2*et)
    r=f.readline()

plt.plot(xa,ya,'o-',label="Numerics",color='red')
plt.plot(xa,ta,label="Theory",color='blue')
plt.plot(xa,spa,'r',alpha=0.2,label="Uncertainty")
plt.plot(xa,sna,'r',alpha=0.2)
plt.fill_between(xa,spa,sna,color='crimson',alpha=0.1)
#plt.legend(loc="lower right", prop={'size': 10})
plt.yscale('log')
plt.text(0.01, 0.03, 'c', horizontalalignment='center',
     verticalalignment='center')
f.close()

plt.xlabel("RIN")
#---------------------------------------------------------------------
plt.subplot(2,2,3)

h0=200

print(3/5)
tpi=2

filestr="0508_2p_2.txt"
f=open(filestr,"r")
xa=[]
ya=[]
ta=[]
spa=[]
sna=[]
omegar=2*np.pi*(1e6)
h_g=200
for i in range(8):
    rtmp=f.readline()
for i in range(10):
    r=f.readline()
    r=f.readline()
    r=f.readline()
    y=r.split()
    print("y="+str(y))
    xa.append(0.01*(i+1))
    ya.append(1-float(y[0]))
    spa.append(0)
    sna.append(0)
##    if(i==40):
##        x=1
    fg=float(x)*(1e6)

    #print(2*omegag**2*sg/(omegar**2))
    N=1/1
    et=N**2*(np.pi)**2*(0.02*(i+1))**2/4
    ta.append(2*et)
    r=f.readline()

plt.plot(xa,ya,'o-',label="Numerics",color='red')
plt.plot(xa,ta,label="Theory",color='blue')
plt.plot(xa,spa,'r',alpha=0.2,label="Uncertainty")
plt.plot(xa,sna,'r',alpha=0.2)
plt.fill_between(xa,spa,sna,color='crimson',alpha=0.1)
#plt.legend(loc="lower right", prop={'size': 10})
plt.yscale('log')
plt.text(0.01, 0.09, 'b', horizontalalignment='center',
     verticalalignment='center')

plt.xlabel("RIN")
plt.ylabel('Error')
f.close()


plt.subplot(2,2,4)
tpi=2
filestr="0508_2p_2w.txt"
f=open(filestr,"r")
xa=[]
ya=[]
ta=[]
spa=[]
sna=[]
omegar=2*np.pi*(1e6)
h_g=200
for i in range(8):
    rtmp=f.readline()
for i in range(10):
    r=f.readline()
    r=f.readline()
    r=f.readline()
    y=r.split()
    print("y="+str(y))
    xa.append(0.01*(i+1))
    ya.append(1-float(y[0]))
    spa.append(0)
    sna.append(0)
##    if(i==40):
##        x=1
    fg=float(x)*(1e6)

    #print(2*omegag**2*sg/(omegar**2))
    N=1/1
    et=N**2*(np.pi)**2*(0.02*(i+1))**2/4
    ta.append(2*et)
    r=f.readline()


plt.plot(xa,ya,'o-',label="Numerics",color='red')
plt.plot(xa,ta,label="Theory",color='blue')
plt.plot(xa,spa,'r',alpha=0.2,label="Uncertainty")
plt.plot(xa,sna,'r',alpha=0.2)
plt.fill_between(xa,spa,sna,color='crimson',alpha=0.1)
plt.legend(loc="lower right", prop={'size': 10})
plt.yscale('log')
plt.text(0.01, 0.09, 'd', horizontalalignment='center',
     verticalalignment='center')
f.close()

plt.xlabel("RIN")


plt.savefig('int_2p_0508.png')


plt.show()
