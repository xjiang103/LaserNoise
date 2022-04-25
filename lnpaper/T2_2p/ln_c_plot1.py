import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from scipy.optimize import curve_fit
matplotlib.rcParams.update({'font.size': 12})
fig = plt.figure()
fig.set_size_inches(3.375,3.375*1)

data = np.loadtxt("ln_c_32.txt")
lw_arr=data[:,0]*1000
print(lw_arr)
t2_arr=data[:,1]
lwfit_arr=np.linspace(0,100,1000)

def func(x,a):
    return a*(1/pow(x,1))

popt,pcov=curve_fit(func,lw_arr,t2_arr)
aaa=popt[0]
t2fit_arr=func(lwfit_arr,aaa)
print(aaa)
print(1000/(2*np.pi))
theoconst=1000/(4*np.pi)
t2theo_arr=func(lwfit_arr,theoconst)


plt.clf()
plt.plot(lw_arr,t2_arr,'ro',label="T2,numerics")
#plt.plot(lwfit_arr,t2fit_arr,'g')
plt.plot(lwfit_arr,t2theo_arr,label="Theory")

plt.xlabel("Linewidth/kHz")
plt.ylabel("T2/μs")
plt.title("T2-Linewidth")
plt.legend(loc="upper right",prop={'size': 10})
plt.xlim([0,110])
plt.ylim([0,4])
plt.show()
plt.savefig("T2_2p.pdf",dpi=300)
