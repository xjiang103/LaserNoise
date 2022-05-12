import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 12})
fig = plt.figure()
fig.set_size_inches(3.375,3.375*2)

gs = fig.add_gridspec(2, hspace=0)
axs = gs.subplots(sharex=True, sharey=False)

tpnum=1
filestr="fmaxswp_0102_"+str(tpnum)+".txt"
f=open(filestr,"r")
xa=[]
ya=[]
siga=[]
spa=[]
sna=[]
for i in range(25):
    r=f.readline()
    x,y,sig=r.split()
    print(str(i)+" "+x+" "+y+" "+sig)
    xa.append(float(x)/1000)
    ya.append(float(y))
    siga.append(float(sig))
f.close()

axs[0].plot(xa,ya,'o',label="Numerics",color='red')
axs[0].plot(xa,siga,label="Theory")
##axs[0].plot(xa,spa,'r',alpha=0.2,label="Uncertainty")
##axs[0].plot(xa,sna,'r',alpha=0.2)
##axs[0].fill_between(xa,spa,sna,color='crimson',alpha=0.1)
axs[0].legend(loc="lower right", prop={'size': 10})
axs[0].set_yscale('log')
if (tpnum==1):
    plt.ylim(10**(-3),10**(-1))
axs[0].text(0.1, 0.9, 'a', horizontalalignment='center',
     verticalalignment='center', transform=axs[0].transAxes)

tpnum=2
filestr="fmaxswp_0102_"+str(tpnum)+".txt"
f=open(filestr,"r")
xa=[]
ya=[]
siga=[]
spa=[]
sna=[]
for i in range(25):
    r=f.readline()
    x,y,sig=r.split()
    print(str(i)+" "+x+" "+y+" "+sig)
    xa.append(float(x)/1000)
    ya.append(float(y))
    siga.append(float(sig))
f.close()

axs[1].plot(xa,ya,'o',label="Numerics",color='red')
axs[1].plot(xa,siga,label="Theory")
##axs[1].plot(xa,spa,'r',alpha=0.2,label="Uncertainty")
##axs[1].plot(xa,sna,'r',alpha=0.2)
##axs[1].fill_between(xa,spa,sna,color='crimson',alpha=0.1)
axs[1].legend(loc="lower right", prop={'size': 10})
axs[1].set_yscale('log')
axs[1].text(0.1, 0.9, 'b', horizontalalignment='center',
     verticalalignment='center', transform=axs[1].transAxes)
if (tpnum%2==0):
    plt.ylim(10**(-6),10**(-2))

    
plt.ylabel('Error')
plt.xlabel("Linewidth (kHz)")
#plt.title("T="+str(tpnum)+"π/Ω")

fig.show()
filestr='quasi_2p.pdf'
plt.savefig(filestr, bbox_inches='tight')

