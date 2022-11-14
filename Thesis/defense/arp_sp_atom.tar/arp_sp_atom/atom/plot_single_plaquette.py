import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams.update({'font.size': 16})

dat = np.loadtxt("arp_data.dat")

plt.clf()
plt.plot(dat[:,0],dat[:,2],"o-",lw=2)
plt.xlabel("Rydberg Coupling")
plt.ylabel("Fidelity")
plt.tight_layout()
plt.title("Single Plaquette")
plt.tight_layout()
plt.savefig("single_plaquette.png",dpi=300)
plt.savefig("single_plaquette.eps")


plt.clf()
plt.plot(dat[:,0],dat[:,1],"o-",lw=2)
plt.xlabel("Rydberg Coupling")
plt.ylabel("Fidelity")
plt.tight_layout()
plt.title("Single Gate")
plt.tight_layout()
plt.savefig("two_atoms.png",dpi=300)
plt.savefig("two_atoms.eps")



plt.clf()
plt.plot(dat[:,0],dat[:,1],"o-",lw=2,label="Single Gate")
plt.plot(dat[:,0],dat[:,1]**8,"o-",lw=2,label="Single Gate")
plt.plot(dat[:,0],dat[:,2],"o-",lw=2,label="Plaquette")
plt.xlabel("Rydberg Coupling")
plt.ylabel("Fidelity")
plt.tight_layout()
plt.title("ARP Gate")
plt.legend()
plt.tight_layout()
plt.savefig("gate_and_plaquette.png",dpi=300)
plt.savefig("gate_and_plaquette.eps")



