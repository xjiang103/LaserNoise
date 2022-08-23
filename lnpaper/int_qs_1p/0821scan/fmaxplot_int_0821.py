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
    f=open("intswp1_1_scan_0821_mix.txt","r")
    omega0=2*np.pi*1000000
    #nnn=1.00001
    bwa=[]
    ya=[]
    sna=[]
    spa=[]
    quasi=[]

    yquasi=[]
    for i in range(40):
        r=f.readline()
        x,y,sp,sn=r.split()
        bwa.append(float(x))
        ya.append(float(y))
        N=1/2
        et=N**2*(np.pi)**2*(1.414*0.05)**2/4
        print(et)
        quasi.append(et)


    plt.plot(bwa,ya,'o-',label="Numerics",color='red')
    plt.plot(bwa,quasi,color='green')
    #plt.plot(xa,y2a,'-',label="Mark_static, bw="+str(nnn)+"Ω",color='blue')
    #plt.plot(bwa,y3a,'-',label="Master Equation",color='blue')
    #plt.plot(bwa,yquasi,'-',label="Static Gaussian",color='green')



plt.yscale('log')
#plt.xscale('log')
plt.legend(loc="lower right", prop={'size': 10})
plt.ylabel('Error')
plt.xlabel(r"$2\pi f_c/\Omega_0$")
filestr="int_fixsigma_bswp_1pi.pdf"
plt.savefig(filestr, bbox_inches='tight',dpi=100)
plt.show()



