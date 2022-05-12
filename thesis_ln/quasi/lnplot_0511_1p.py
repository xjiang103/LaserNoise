import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 12})


fig = plt.figure()
fig.set_size_inches(3.375*2,3.375*1)

gs = fig.add_gridspec(1,2, hspace=0)
axs = gs.subplots(sharex=False, sharey=False)

tpi=1
f=open("fmaxswp_0118_1.txt","r")
xa=[]
y1a=[]
y2a=[]
for i in range(80):
    r=f.readline()
    x,y1,y2,sn,sp=r.split()
    print(str(i)+" "+x+" "+y1+" "+y2)
    xa.append(float(x)/1000000)
    y1a.append(float(y1))
    y2a.append(float(y2))

axs[0].plot(xa,y1a,'o-',label="Numerics",color='red')
axs[0].plot(xa,y2a,'-',label="Theory",color='blue')
axs[0].set_yscale('log')
axs[0].legend(loc="lower right")
axs[0].text(0.1, 0.9, 'a', horizontalalignment='center',
     verticalalignment='center', transform=axs[0].transAxes)
axs[0].set_ylabel('Error')
axs[0].set_xlabel("Bandwidth/($Ω_0$/2π))")
tpi=2
f=open("fmaxswp_0118_2.txt","r")
xa=[]
y1a=[]
y2a=[]
for i in range(80):
    r=f.readline()
    x,y1,y2,sn,sp=r.split()
    print(str(i)+" "+x+" "+y1+" "+y2)
    xa.append(float(x)/1000000)
    y1a.append(float(y1))
    y2a.append(float(y2))

axs[1].plot(xa,y1a,'o-',label="Numerics",color='red')
axs[1].plot(xa,y2a,'-',label="Theory",color='blue')
axs[1].set_yscale('log')
axs[1].legend(loc="lower right", prop={'size': 10})
axs[1].text(0.1, 0.9, 'b', horizontalalignment='center',
     verticalalignment='center', transform=axs[1].transAxes)
#axs[1].set_ylabel('Error')
axs[1].set_xlabel("Bandwidth/($Ω_0$/2π))")


fig.show()


filestr='fmaxswp_thesis.pdf'
plt.savefig(filestr, bbox_inches='tight',dpi=100)
