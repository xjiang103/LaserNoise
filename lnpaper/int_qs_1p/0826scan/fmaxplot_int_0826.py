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
    #plt.plot(xa,y2a,'-',label="Mark_static, bw="+str(nnn)+"Ω",color='blue')
    #plt.plot(bwa,y3a,'-',label="Master Equation",color='blue')
    #plt.plot(bwa,yquasi,'-',label="Static Gaussian",color='green')



plt.yscale('log')
plt.xscale('log')
plt.legend(loc="lower left", prop={'size': 10})
plt.ylabel('Error')
plt.xlabel(r"$2\pi f_c/\Omega_0$")
filestr="1pi_intfcswp.pdf"
plt.savefig(filestr, bbox_inches='tight',dpi=100)
plt.show()



