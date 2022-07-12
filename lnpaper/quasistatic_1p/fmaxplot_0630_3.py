import matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.rcParams.update({'font.size': 12})

fig = plt.figure()
fig.set_size_inches(3.375,3.375*2)

gs = fig.add_gridspec(1, hspace=0)
axs = gs.subplots(sharex=True, sharey=True)

tpi=2

bwar=[1.0,2.0,
      2.5,3.0,3.5,4.0]
bwar=[100,300,3000,10000,30000,100000]
nnn=0
y3a=[]
nr=0
for k in range(6):
    nnn=0.01
    nr=bwar[k]
    f=open("fmaxswp_0628_"+str(nr)+".txt","r")
    omega0=2*np.pi*1000000

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
        y2a.append(ff1)
        y3a.append(ff2/(1))
        
        yquasi.append(quas)
    #plt.plot(xa,spa,'r',alpha=0.2,label="Uncertainty")
    #plt.plot(xa,sna,'r',alpha=0.2)
    plt.plot(xa,y1a,'o-',label="Numerics, "+str(nr)+"runs")
    #plt.plot(xa,y2a,'-',label="Mark_static, bw="+str(nnn)+"Ω",color='blue')
    #plt.fill_between(xa,spa,sna,color='crimson',alpha=0.1)
    #plt.plot(xa,yquasi,'-',label="Xiaoyu, bw="+str(nnn)+"Ω",color='green')
#plt.plot(xa,y2a,'-',label="Mark 2-term Theory",color='purple')
#plt.plot(xa,y3a,'-',label="Mark 1-term Theory",color='blue')

#plt.plot(xa,y3a,'-',label="Mark_wide",color='black')

plt.yscale('log')
plt.xscale('log')
plt.legend(loc="lower right", prop={'size': 10})
plt.ylabel('Error')
plt.xlabel("h/kHz")
filestr="fs_0630_bwswp_"+str(nr)+".png"
plt.savefig(filestr, bbox_inches='tight',dpi=100)
plt.show()



