import matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.rcParams.update({'font.size': 12})
fig = plt.figure()
fig.set_size_inches(3.375*2,3.375*1)

gs = fig.add_gridspec(1, 2, hspace=0)
axs = gs.subplots(sharex=True, sharey=False)

print(3/5)
tpi=1

filestr="f3swp1_0102.txt"
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

for i in range(78):
    r=f.readline()
    x,y,sp,sn=r.split()
    print(str(i)+" "+x+" "+y)
    xa.append(float(x))
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
    print(omegag/omegar)
    et=2*omegag**2*sg*(1/omegar**2)*((np.cos(0.5*np.pi*omegag/omegar))**2*\
        (1-(-1)**(2*N)*np.cos(2*np.pi*N*omegag/omegar))/(4*(omegar**2-omegag**2)**2/omegar**4)+\
        (np.sin(0.5*np.pi*omegag/omegar))**2*2*np.pi*N*(1+2*np.pi*N)/32)
    et=2*sg*(np.pi*fg*omegar)**2*(1)*\
        (1-(-1)**(2*N)*np.cos(4*np.pi**2*N*fg/omegar))/(omegar**2-omegag**2)**2
    
    print(sg)
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
axs[0].set_xlabel("$f_g$/($Ω_0$/2π))")
axs[0].set_ylabel('Error')

tpi=2
filestr="f3swp2_0102.txt"
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
r=f.readline()
r=f.readline()
for i in range(76):
    r=f.readline()
    x,y,sp,sn=r.split()
    print(str(i)+" "+x+" "+y)
    xa.append(float(x))
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
    print(omegag/omegar)
    et=2*omegag**2*sg*(1/omegar**2)*((np.cos(0.5*np.pi*omegag/omegar))**2*\
        (1-(-1)**(2*N)*np.cos(2*np.pi*N*omegag/omegar))/(4*(omegar**2-omegag**2)**2/omegar**4)+\
        (np.sin(0.5*np.pi*omegag/omegar))**2*2*np.pi*N*(1+2*np.pi*N)/32)
    et=2*sg*(np.pi*fg*omegar)**2*(1)*\
        (1-(-1)**(2*N)*np.cos(4*np.pi**2*N*fg/omegar))/(omegar**2-omegag**2)**2
    
    print(sg)
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

axs[1].set_xlabel("$f_g$/($Ω_0$/2π))")

fig.show()

plt.savefig('fg_2p_thesis.pdf', bbox_inches='tight')

