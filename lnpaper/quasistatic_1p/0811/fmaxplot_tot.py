import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import scipy
from scipy import special

matplotlib.rcParams.update({'font.size': 12})
fig = plt.figure()
fig.set_size_inches(3.375,3.375*2)

gs = fig.add_gridspec(2, hspace=0)
axs = gs.subplots(sharex=True, sharey=False)



tpi=2

bwar=[1.0,2.0,
      2.5,3.0,3.5,4.0]
bwar=[0.1]
nnn=0.03
y3a=[]
for k in range(1):
    nnn=bwar[k]
    f=open("fb_10k_0807.txt","r")
    omega0=2*np.pi*1000000
    #nnn=1.00001
    bwa=[]
    y1a=[]
    y2a=[]
    y3a=[]

    yquasi=[]
    for i in range(29):
        N=0.5
        r=f.readline()
        x,y1,bw=r.split()
        #print(str(i)+" "+x+" "+y1+" "+y2)
        bwa.append(float(bw))
        y1a.append(float(y1))
        nnn=float(bw)
        xnum=float(x)/np.pi
        sig=np.sqrt((1/1)*2*xnum*nnn*omega0/(2*np.pi))/(omega0/(2*np.pi))
        quas=0.75*(np.pi/1)**2*sig**4
        ff1=8*np.pi**2*xnum*(nnn*omega0/(2*np.pi))/(omega0**2)
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
        
        yquasi.append(ff1)

    axs[0].plot(bwa,y1a,'o-',label="Numerics",color='red')
    #plt.plot(xa,y2a,'-',label="Mark_static, bw="+str(nnn)+"Ω",color='blue')
    axs[0].plot(bwa,y3a,'-',label="Master Equation",color='blue')
    axs[0].plot(bwa,yquasi,'-',label="Static Gaussian",color='green')
    axs[0].set_xscale('log')
    axs[0].set_yscale('log')
    axs[0].legend(loc="lower right", prop={'size': 10})
    axs[0].text(0.1, 0.9, 'a', horizontalalignment='center',
     verticalalignment='center', transform=axs[0].transAxes)
    #plt.axvline(x = 0.014276, color = 'orange',linestyle='dashed')
    #plt.text(0.0032,0.001, r'$f_c=1.43h$')
#plt.plot(xa,y2a,'-',label="Mark 2-term Theory",color='purple')
#plt.plot(xa,y3a,'-',label="Mark 1-term Theory",color='blue')

for k in range(1):
    nnn=bwar[k]
    f=open("fb_10k.txt","r")
    omega0=2*np.pi*1000000
    #nnn=1.00001
    bwa=[]
    y1a=[]
    y2a=[]
    y3a=[]

    yquasi=[]
    for i in range(29):
        N=1
        r=f.readline()
        x,y1,bw=r.split()
        #print(str(i)+" "+x+" "+y1+" "+y2)
        bwa.append(float(bw))
        y1a.append(float(y1))
        nnn=float(bw)
        xnum=float(x)/np.pi
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

    axs[1].plot(bwa,y1a,'o-',label="Numerics",color='red')
    #plt.plot(xa,y2a,'-',label="Mark_static, bw="+str(nnn)+"Ω",color='blue')
    axs[1].plot(bwa,y3a,'-',label="Master Equation",color='blue')
    axs[1].plot(bwa,yquasi,'-',label="Static Gaussian",color='green')
    axs[1].axvline(x = 0.014276, color = 'orange',linestyle='dashed')
    axs[1].set_xscale('log')
    axs[1].set_yscale('log')
    axs[1].legend(loc="lower right", prop={'size': 10})
    axs[1].text(0.1, 0.9, 'b', horizontalalignment='center',
     verticalalignment='center', transform=axs[1].transAxes)
    #plt.text(0.0032,0.001, r'$f_c=1.43h$')
#plt.plot(xa,y2a,'-',label="Mark 2-term Theory",color='purple')
#plt.plot(xa,y3a,'-',label="Mark 1-term Theory",color='blue')


plt.ylabel('Error')
plt.xlabel(r"$2\pi f_c/\Omega_0$")
filestr="fixh_bswp_tot.pdf"
plt.savefig(filestr, bbox_inches='tight',dpi=100)
plt.show()



