import matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.rcParams.update({'font.size': 12})
fig = plt.figure()
fig.set_size_inches(3.375,3.375*2)

gs = fig.add_gridspec(2, hspace=0)
axs = gs.subplots(sharex=True, sharey=False)

h0=200

print(3/5)
tpi=1

filestr="f3swp1_0407.txt"
f=open(filestr,"r")
xa=[]
ya=[]
ta=[]
spa=[]
sna=[]
omegar=2*np.pi*(1e6)
h_g=1100
f_g0=234*(1e3)
sigma_g=1.4*(1e3)

for i in range(18):
    r=f.readline()
    x,y,sp,sn=r.split()
    print(str(i)+" "+x+" "+y)
    xa.append(200*(i+1))
    ya.append(float(y))
    spa.append(float(y)+float(sp))
    sna.append(float(y)*0.5)
##    if(i==40):
##        x=1
    fg=float(x)*(1e6)
    omegag=2*np.pi*fg
    sg=np.sqrt(8*np.pi)*sigma_g*h_g/(f_g0**2)
    #print(2*omegag**2*sg/(omegar**2))
    N=1/2
    et=h0*(i+1)*(np.pi**3+np.pi**2*N+2*np.pi**3*N**2)/omegar
    et=(1)*h0*(i+1)*N*np.pi**3/omegar
    ta.append(2*et)


axs[0].plot(xa,ya,'o-',label="Numerics",color='red')
axs[0].plot(xa,ta,label="Theory",color='blue')
axs[0].plot(xa,spa,'r',alpha=0.2,label="Uncertainty")
axs[0].plot(xa,sna,'r',alpha=0.2)
axs[0].fill_between(xa,spa,sna,color='crimson',alpha=0.1)
axs[0].legend(loc="lower right", prop={'size': 10})
axs[0].set_yscale('log')
axs[0].text(0.1, 0.9, 'a', horizontalalignment='center',
     verticalalignment='center', transform=axs[0].transAxes)
f.close()

tpi=2
filestr="f3swp2_0407.txt"
f=open(filestr,"r")
xa=[]
ya=[]
ta=[]
spa=[]
sna=[]
omegar=2*np.pi*(1e6)
h_g=1100
f_g0=234*(1e3)
sigma_g=1.4*(1e3)

for i in range(18):
    r=f.readline()
    x,y,sp,sn=r.split()
    print(str(i)+" "+x+" "+y)
    xa.append(200*(i+1))
    ya.append(float(y))
    spa.append(float(y)+float(sp))
    sna.append(float(y)*0.5)
##    if(i==40):
##        x=1
    fg=float(x)*(1e6)
    omegag=2*np.pi*fg
    sg=np.sqrt(8*np.pi)*sigma_g*h_g/(f_g0**2)
    #print(2*omegag**2*sg/(omegar**2))
    N=1/1
    et=h0*(i+1)*(np.pi**3+np.pi**2*N+2*np.pi**3*N**2)/omegar
    et=(1)*h0*(i+1)*N*np.pi**3/omegar
    ta.append(2*et)


axs[1].plot(xa,ya,'o-',label="Numerics",color='red')
axs[1].plot(xa,ta,label="Theory",color='blue')
axs[1].plot(xa,spa,'r',alpha=0.2,label="Uncertainty")
axs[1].plot(xa,sna,'r',alpha=0.2)
axs[1].fill_between(xa,spa,sna,color='crimson',alpha=0.1)
axs[1].legend(loc="lower right", prop={'size': 10})
axs[1].set_yscale('log')
axs[1].text(0.1, 0.9, 'b', horizontalalignment='center',
     verticalalignment='center', transform=axs[1].transAxes)
f.close()

plt.xlabel("$h_0$")
plt.ylabel('Error')
fig.show()

plt.savefig('wn_2p_0419.pdf', bbox_inches='tight')

