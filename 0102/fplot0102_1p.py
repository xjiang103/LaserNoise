import matplotlib.pyplot as plt
import matplotlib
tpnum=2
matplotlib.rcParams.update({'font.size': 18})
plt.rcParams["figure.figsize"] = (3.375,2.875)
filestr="fmaxswp_1103_"+str(tpnum)+".txt"
f=open(filestr,"r")
xa=[]
ya=[]
siga=[]
spa=[]
sna=[]
for i in range(25):
    r=f.readline()
    x,y,sig,sp,sn=r.split()
    print(str(i)+" "+x+" "+y+" "+sig)
    xa.append(float(x)/1000)
    ya.append(float(y))
    siga.append(float(sig))
    spa.append(float(y)+float(sp))
    sna.append(float(y)-float(sn))
f.close()

plt.plot(xa,ya,'o',label="Numerics",color='red')
plt.plot(xa,siga,label="Theory")
plt.plot(xa,spa,'r',alpha=0.2,label="Uncertainty")
plt.plot(xa,sna,'r',alpha=0.2)
plt.fill_between(xa,spa,sna,color='crimson',alpha=0.1)
plt.legend(loc="lower right", prop={'size': 12})
plt.yscale('log')
if (tpnum%2==0):
    plt.ylim(10**(-8),10**(-3))
plt.ylabel('Error')
plt.xlabel("Bandwidth (kHz)")
#plt.title("T="+str(tpnum)+"π/Ω")
filestr='quasi_1p_'+str(tpnum)+'pi.pdf'
plt.savefig(filestr, bbox_inches='tight')

