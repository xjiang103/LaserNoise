import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.rcParams.update({'font.size': 16})
print(3/5)
f=open("f3swp10_0630.txt","r")
xa=[]
ya=[]
ta=[]
hg0=1100
fg0=234*(1e3)
omegar=(1e6)*2*np.pi
n=1
sigmag=1.4*(1e3)
sigman=0.0407*omegar/n
    
for i in range(20):
    
    scale_fac=0.5*(i+1)
    hg=hg0*(scale_fac**2)
    fg=fg0*(scale_fac)
    
    
    r=f.readline()
    x,y=r.split()
    xa.append(float(x))
    ya.append(float(y))
    errest=3*(np.pi)**3*n*hg*sigmag/(2*omegar*np.sqrt(sigmag**2+sigman**2))
    errest=errest*np.exp(-(omegar/(2*np.pi)-fg)**2/(2*(sigmag**2+sigman**2)))
    ta.append(errest)
#plt.plot(xa,ya,'o-',label="Numerics")
plt.plot(xa,ta,'o-',label="Estimate")
##for i in range(int(116)):
##    plt.plot([xa[i],xa[i]],[ya[i]-sdna[i],ya[i]+sdpa[i]],'r')
f.close()
plt.xlabel("fbump/(ΩR/2π))")
plt.ylabel('error')
plt.title("2-photon Pi pulse error")
plt.legend(loc="upper right")

plt.show()

