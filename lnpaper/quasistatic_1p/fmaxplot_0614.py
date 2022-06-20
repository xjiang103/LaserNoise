import matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.rcParams.update({'font.size': 12})
nnn=0.002
fig = plt.figure()
fig.set_size_inches(3.375,3.375*2)

gs = fig.add_gridspec(2, hspace=0)
axs = gs.subplots(sharex=True, sharey=True)

tpi=2
omega0=2*np.pi*1000000
f=open("fmaxswp_0619_500_"+str(nnn)+".txt","r")
xa=[]
y1a=[]
y2a=[]
for i in range(25):
    r=f.readline()
    x,y1,y2,sn,sp=r.split()
    #print(str(i)+" "+x+" "+y1+" "+y2)
    xa.append(float(x)/1000000)
    y1a.append(float(y1))
    xnum=float(x)
    sig=np.sqrt((1/np.pi)*2*xnum*nnn*omega0/(2*np.pi))/(omega0/(2*np.pi))
    quas=0.75*(np.pi/1)**2*sig**4
    #print(float(y2)/quas)
    ff=32*np.pi**6*xnum*(0.01*omega0/(2*np.pi))**3*1/(3*omega0**4)
    y2a.append(quas)

axs[0].plot(xa,y1a,'o-',label="Numerics",color='red')
axs[0].plot(xa,y2a,'-',label="Theory",color='blue')
axs[0].set_yscale('log')
axs[0].set_xscale('log')
axs[0].legend(loc="lower right")
axs[0].text(0.1, 0.9, 'a', horizontalalignment='center',
     verticalalignment='center', transform=axs[0].transAxes)

tpi=2
f=open("fmaxswp_0619_500_"+str(nnn)+".txt","r")
xa=[]
y1a=[]
y2a=[]
for i in range(25):
    N=1
    r=f.readline()
    x,y1,y2,sn,sp=r.split()
    #print(str(i)+" "+x+" "+y1+" "+y2)
    xa.append(float(x)/1000000)
    y1a.append(float(y1))
    xnum=float(x)
    ff1=32*np.pi**6*xnum*(nnn*omega0/(2*np.pi))**3*1/(3*omega0**4)
    ff2=10000*N*np.pi**3/omega0
    y2a.append(ff1)

axs[1].plot(xa,y1a,'o-',label="Numerics",color='red')
axs[1].plot(xa,y2a,'-',label="Theory",color='blue')
axs[1].set_yscale('log')
axs[0].set_xscale('log')
axs[1].legend(loc="lower right", prop={'size': 10})
axs[1].text(0.1, 0.9, 'b', horizontalalignment='center',
     verticalalignment='center', transform=axs[1].transAxes)
plt.ylabel('Error')
plt.xlabel("Bandwidth/($Ω_0$/2π))")


fig.show()


filestr="fmaxswp_0620_500_"+str(nnn)+".png"
plt.savefig(filestr, bbox_inches='tight',dpi=100)