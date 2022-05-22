import matplotlib.pyplot as plt
import numpy as np
import matplotlib

matplotlib.rcParams.update({'font.size': 12})
fig = plt.figure()
fig.set_size_inches(3.375*2,3.375)

gs = fig.add_gridspec(1,2, hspace=0)
axs = gs.subplots(sharex=True, sharey=False)

print(3/5)
tpi=1
filestr="hgswp_1031_"+str(tpi)+".txt"
f=open(filestr,"r")
xa=[]
ya=[]
stdpa=[]
stdna=[]
    
for i in range(5):
    r=f.readline()
    x,y,stdp,stdn=r.split()
    xa.append(float(x))
    ya.append(float(y))
    stdpa.append(float(y)+float(stdp))
    stdna.append(float(y)-float(stdn))

axs[0].plot(xa,ya,'o-',label="Error",color='red')
axs[0].plot(xa,stdpa,'r',alpha=0.2,label="Uncertainty")
axs[0].plot(xa,stdna,'r',alpha=0.2)
#for i in range(5):
#    plt.plot([xa[i],xa[i]],[stdna[i],stdpa[i]],'r')
axs[0].fill_between(xa,stdpa,stdna,color='crimson',alpha=0.1)
##for i in range(int(116)):
##    plt.plot([xa[i],xa[i]],[ya[i]-sdna[i],ya[i]+sdpa[i]],'r')
f.close()
axs[0].set_yscale('log')
axs[0].set_xscale('log')
axs[0].text(0.1, 0.9, 'a', horizontalalignment='center',
     verticalalignment='center', transform=axs[0].transAxes)
axs[0].legend(loc="lower right", prop={'size': 12})
axs[0].set_xlabel("Fractional Power")
axs[0].set_ylabel('Error')



tpi=2
filestr="hgswp_1031_"+str(tpi)+".txt"
f=open(filestr,"r")
xa=[]
ya=[]
stdpa=[]
stdna=[]
    
for i in range(5):
    r=f.readline()
    x,y,stdp,stdn=r.split()
    xa.append(float(x))
    ya.append(float(y))
    stdpa.append(float(y)+float(stdp))
    stdna.append(float(y)-float(stdn))

axs[1].plot(xa,ya,'o-',label="Error",color='red')
axs[1].plot(xa,stdpa,'r',alpha=0.2,label="Uncertainty")
axs[1].plot(xa,stdna,'r',alpha=0.2)
#for i in range(5):
#    plt.plot([xa[i],xa[i]],[stdna[i],stdpa[i]],'r')
axs[1].fill_between(xa,stdpa,stdna,color='crimson',alpha=0.1)
##for i in range(int(116)):
##    plt.plot([xa[i],xa[i]],[ya[i]-sdna[i],ya[i]+sdpa[i]],'r')
f.close()
axs[1].set_yscale('log')
axs[1].set_xscale('log')
axs[1].text(0.1, 0.9, 'b', horizontalalignment='center',
     verticalalignment='center', transform=axs[1].transAxes)
axs[1].legend(loc="lower right", prop={'size': 10})

axs[1].set_xlabel("Fractional Power")

#plt.title("Error at time "+str(tpi)+"π/Ω")


filestr='pwrswp_thesis.pdf'
plt.savefig(filestr, bbox_inches='tight',dpi=100)

