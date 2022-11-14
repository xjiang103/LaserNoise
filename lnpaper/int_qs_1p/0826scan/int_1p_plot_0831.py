import matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.rcParams.update({'font.size': 10})


plt.subplot(2,2,1)

h0=200

print(3/5)
tpi=1

filestr="intswp1_1.txt"
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
    print(sna[i]/ya[i])
##    if(i==40):
##        x=1
    fg=float(x)*(1e6)

    #print(2*omegag**2*sg/(omegar**2))
    N=1/2
    et=N**2*(np.pi)**2*(0.02*(i+1))**2/4
    ta.append(1*et)


plt.plot(xa,ya,'o-',label="Numerics",color='red')
plt.plot(xa,ta,label="Theory",color='blue')
plt.plot(xa,spa,'r',alpha=0.2,label="Uncertainty")
plt.plot(xa,sna,'r',alpha=0.2)
plt.fill_between(xa,spa,sna,color='crimson',alpha=0.1)
#plt.legend(loc="lower right", prop={'size': 10})
plt.yscale('log')
plt.text(0.01, 0.06, 'a', horizontalalignment='center',
     verticalalignment='center')

plt.ylabel('Error')
f.close()

#------------------------------------------------------------------------------

plt.subplot(2,2,2)

for k in range(1):
    nnn=0.1
    f=open("intswp1_1_scan_0826.txt","r")
    omega0=2*np.pi*1000000
    #nnn=1.00001
    bwa=[]
    ya=[]
    sna=[]
    spa=[]
    quasi=[]

    yquasi=[]
    for i in range(200):
        r=f.readline()
        x,y,sp,sn=r.split()
        bwa.append(float(x)/1000000)
        ya.append(float(y))
        spa.append(float(y)+float(sp))
        sna.append(float(y)-float(sn))
        N=1/2
        et=N**2*(np.pi)**2*(1.414*0.05)**2/4
        #print(et)
        quasi.append(et)


    plt.plot(bwa,ya,'o-',label="Numerics",color='red')
    plt.plot(bwa,quasi,color='blue',label="Theory")
    plt.plot(bwa,spa,'r',alpha=0.2,label="Uncertainty")
    plt.plot(bwa,sna,'r',alpha=0.2)
    plt.fill_between(bwa,spa,sna,color='crimson',alpha=0.1)
    plt.text(0.01, 0.012, 'b', horizontalalignment='center',
     verticalalignment='center')
    #plt.plot(xa,y2a,'-',label="Mark_static, bw="+str(nnn)+"Ω",color='blue')
    #plt.plot(bwa,y3a,'-',label="Master Equation",color='blue')
    #plt.plot(bwa,yquasi,'-',label="Static Gaussian",color='green')



plt.yscale('log')
plt.xscale('log')
#plt.legend(loc="lower left", prop={'size': 10})

f.close()

#---------------------------------------------------------------------
plt.subplot(2,2,3)

h0=200

print(3/5)
tpi=2

filestr="intswp1_2.txt"
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
    N=1/1
    et=N**2*(np.pi)**2*(0.02*(i+1))**2/4
    ta.append(1*et)


plt.plot(xa,ya,'o-',label="Numerics",color='red')
plt.plot(xa,ta,label="Theory",color='blue')
plt.plot(xa,spa,'r',alpha=0.2,label="Uncertainty")
plt.plot(xa,sna,'r',alpha=0.2)
plt.fill_between(xa,spa,sna,color='crimson',alpha=0.1)
#plt.legend(loc="lower right", prop={'size': 10})
plt.yscale('log')
plt.text(0.01, 0.2, 'b', horizontalalignment='center',
     verticalalignment='center')
plt.legend(loc="lower right", prop={'size': 10})

plt.xlabel(r"$\sigma_{\alpha_I}$")
plt.ylabel('Error')
f.close()


plt.subplot(2,2,4)

for k in range(1):
    nnn=0.1
    f=open("intswp1_2_scan_0826.txt","r")
    omega0=2*np.pi*1000000
    #nnn=1.00001
    bwa=[]
    ya=[]
    sna=[]
    spa=[]
    quasi=[]

    yquasi=[]
    for i in range(200):
        r=f.readline()
        x,y,sp,sn=r.split()
        bwa.append(float(x)/1000000)
        ya.append(float(y))
        spa.append(float(y)+float(sp))
        sna.append(float(y)-float(sn))
        N=2/2
        et=N**2*(np.pi)**2*(1.414*0.05)**2/4
        #print(et)
        quasi.append(et)


    plt.plot(bwa,ya,'o-',label="Numerics",color='red')
    plt.plot(bwa,quasi,color='blue',label="Theory")
    plt.plot(bwa,spa,'r',alpha=0.2,label="Uncertainty")
    plt.plot(bwa,sna,'r',alpha=0.2)
    plt.fill_between(bwa,spa,sna,color='crimson',alpha=0.1)
    plt.text(0.01, 0.035, 'd', horizontalalignment='center',
     verticalalignment='center')
    #plt.plot(xa,y2a,'-',label="Mark_static, bw="+str(nnn)+"Ω",color='blue')
    #plt.plot(bwa,y3a,'-',label="Master Equation",color='blue')
    #plt.plot(bwa,yquasi,'-',label="Static Gaussian",color='green')



plt.yscale('log')
plt.xscale('log')
plt.legend(loc="lower left", prop={'size': 10})
plt.xlabel(r"$2\pi f_c/\Omega_0$")

f.close()


plt.savefig('int_1p_0831.pdf')


plt.show()
