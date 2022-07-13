import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import scipy
from scipy import special

matplotlib.rcParams.update({'font.size': 12})

fig = plt.figure()
fig.set_size_inches(3.375,3.375)

gs = fig.add_gridspec(1, hspace=0)
axs = gs.subplots(sharex=True, sharey=True)

tpi=2

bwar=[1.0,2.0,
      2.5,3.0,3.5,4.0]
bwar=[0.1]
nnn=0.03
y3a=[]
for k in range(1):
    nnn=bwar[k]
    f=open("fmaxswp_0619_500_"+str(nnn)+".txt","r")
    omega0=2*np.pi*1000000
    #nnn=1.00001
    xa=[]
    y1a=[]
    y2a=[]
    y3a=[]
    spa=[]
    sna=[]
    yquasi=[]
    for i in range(25):
        N=1
        r=f.readline()
        x,y1,y2,sn,sp=r.split()
        #print(str(i)+" "+x+" "+y1+" "+y2)
        xa.append(float(x)/1000)
        y1a.append(float(y1))
        xnum=float(x)/np.pi
        spa.append(float(sp))
        sna.append(float(sn))
        sig=np.sqrt((1/1)*2*xnum*nnn*omega0/(2*np.pi))/(omega0/(2*np.pi))
        quas=0.75*(np.pi/1)**2*sig**4
        ff1=32*np.pi**6*xnum*(nnn*omega0/(2*np.pi))**3*1/(3*omega0**4)-128*xnum*(nnn*omega0/(2*np.pi))**5*(np.pi**10*N**4/(6*np.pi**2*N*N))/(15*omega0**6)
        ff2=np.pi**3*xnum*N/omega0

        y=complex(nnn,0)
        si1,ci1=scipy.special.sici(2*np.pi*N*(1-y))
        si2,ci2=scipy.special.sici(2*np.pi*N*(1+y))
        
        fpart=0
        fpart+=2*y*(1-(-1)**(2*N)*np.cos(2*np.pi*N*y))/(1-y*y)
        fpart+=2*np.arctanh(y)
        fpart+=ci1
        fpart=fpart-ci2
        fpart=fpart-2*np.pi*N*si1
        fpart+=2*np.pi*N*si2
        
        ffreal=(np.pi*xnum*0.5/omega0)*fpart
        y2a.append(ff1)
        y3a.append(ffreal/(1))
        
        yquasi.append(quas)
    plt.plot(xa,spa,'r',alpha=0.2,label="Uncertainty")
    plt.plot(xa,sna,'r',alpha=0.2)
    plt.plot(xa,y1a,'o-',label="Numerics, bw="+str(nnn)+"Ω",color='red')
    #plt.plot(xa,y2a,'-',label="Mark_static, bw="+str(nnn)+"Ω",color='blue')
    plt.fill_between(xa,spa,sna,color='crimson',alpha=0.1)
    plt.plot(xa,y3a,'-',label="Master Equation",color='blue')
    plt.plot(xa,yquasi,'-',label="Static Gaussian",color='green')
#plt.plot(xa,y2a,'-',label="Mark 2-term Theory",color='purple')
#plt.plot(xa,y3a,'-',label="Mark 1-term Theory",color='blue')



plt.yscale('log')
plt.xscale('log')
plt.legend(loc="lower right", prop={'size': 10})
plt.ylabel('Error')
plt.xlabel("h/kHz")
filestr="fs_0708_bwswp_"+str(nnn)+".png"
plt.savefig(filestr, bbox_inches='tight',dpi=100)
plt.show()


