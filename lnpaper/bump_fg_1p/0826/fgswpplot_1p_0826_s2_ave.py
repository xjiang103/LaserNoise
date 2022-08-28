import matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.rcParams.update({'font.size': 12})
fig = plt.figure()
fig.set_size_inches(3.375,3.375*2)

gs = fig.add_gridspec(2, hspace=0)
axs = gs.subplots(sharex=True, sharey=False)

print(3/5)
tpi=1

filestr="sig_0826_s2_1.txt"
f=open(filestr,"r")
filestr2="sig_0826_s2m_1.txt"
fm=open(filestr2,"r")
xa=[]
ya=[]
ta=[]
spa=[]
sna=[]
omegar=2*np.pi*(1e6)
h_g=1100
f_g0=234*(1e3)
sigma_g=1.4*(1e3)

for i in range(80):
    r=f.readline()
    x,y,sp,sn=r.split()
    rm=fm.readline()
    xm,ym,spm,snm=rm.split()

    xdat=0.5*(float(x)+float(xm))
    ydat=0.5*(float(y)+float(ym))
    spdat=0.5*(float(sp)+float(spm))
    sndat=0.5*(float(sn)+float(snm))
    
    xa.append(xdat)
    ya.append(ydat)
    spa.append(ydat+spdat)
    sna.append(ydat-sndat)
##    if(i==40):
##        x=1
    fg=xdat*(1e6)
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
    ta.append(1*et)


axs[0].plot(xa,ya,'o-',label="Numerics",color='red')
axs[0].plot(xa,ta,label="Theory",color='blue')
axs[0].plot(xa,spa,'r',alpha=0.2,label="Uncertainty")
axs[0].plot(xa,sna,'r',alpha=0.2)
axs[0].fill_between(xa,spa,sna,color='crimson',alpha=0.1)
axs[0].legend(loc="lower center", prop={'size': 10})
axs[0].set_yscale('log')
axs[0].text(0.1, 0.9, 'a', horizontalalignment='center',
     verticalalignment='center', transform=axs[0].transAxes)
f.close()
fm.close()

tpi=2
filestr="sig_0826_s2_2.txt"
f=open(filestr,"r")
filestr2="sig_0826_s2m_2.txt"
fm=open(filestr2,"r")
xa=[]
ya=[]
ta=[]
spa=[]
sna=[]
omegar=2*np.pi*(1e6)
h_g=1100
f_g0=234*(1e3)
sigma_g=1.4*(1e3)

for i in range(80):
    r=f.readline()
    x,y,sp,sn=r.split()
    rm=fm.readline()
    xm,ym,spm,snm=rm.split()

    xdat=0.5*(float(x)+float(xm))
    ydat=0.5*(float(y)+float(ym))
    spdat=0.5*(float(sp)+float(spm))
    sndat=0.5*(float(sn)+float(snm))
    
    xa.append(xdat)
    ya.append(ydat)
    spa.append(ydat+spdat)
    sna.append(ydat-sndat)
##    if(i==40):
##        x=1
    fg=xdat*(1e6)
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
    ta.append(1*et)


axs[1].plot(xa,ya,'o-',label="Numerics",color='red')
axs[1].plot(xa,ta,label="Theory",color='blue')
axs[1].plot(xa,spa,'r',alpha=0.2,label="Uncertainty")
axs[1].plot(xa,sna,'r',alpha=0.2)
axs[1].fill_between(xa,spa,sna,color='crimson',alpha=0.1)
axs[1].legend(loc="lower center", prop={'size': 10})
axs[1].set_yscale('log')
axs[1].text(0.1, 0.9, 'b', horizontalalignment='center',
     verticalalignment='center', transform=axs[1].transAxes)
f.close()
fm.close()

plt.xlabel("$f_g$/($Ω_0$/2π))")
plt.ylabel('Error')
fig.show()

plt.savefig('y_ave_sig.pdf', bbox_inches='tight')

