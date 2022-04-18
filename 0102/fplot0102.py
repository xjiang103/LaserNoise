import matplotlib.pyplot as plt
import matplotlib
tpnum=2
matplotlib.rcParams.update({'font.size': 24})
filestr="fmaxswp_0102_"+str(tpnum)+".txt"
f=open(filestr,"r")
xa=[]
ya=[]
siga=[]
for i in range(25):
    r=f.readline()
    x,y,sig=r.split()
    print(str(i)+" "+x+" "+y+" "+sig)
    xa.append(float(x)/1000)
    ya.append(float(y))
    siga.append(float(sig))
    #spa.append(float(y)+float(sp))
    #sna.append(float(y)-float(sn))
f.close()

plt.plot(xa,ya,'o',label="numerics",color='red')
plt.plot(xa,siga,label="quasistatic")
#plt.plot(xa,spa,'r',alpha=0.2,label="Uncertainty")
#plt.plot(xa,sna,'r',alpha=0.2)
#plt.fill_between(xa,spa,sna,color='crimson',alpha=0.1)
plt.legend(loc="lower right", prop={'size': 12})
plt.yscale('log')
if (tpnum%2==0):
    plt.ylim(10**(-6),10**(-2))
plt.xlabel("Bandwidth/kHz")
plt.ylabel('Error')
plt.title("T="+str(tpnum)+"π/Ω")
filestr='quasi_2p_'+str(tpnum)+'pi.pdf'
plt.savefig(filestr, bbox_inches='tight')

