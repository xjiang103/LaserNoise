import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams.update({'font.size': 16})

dat = np.loadtxt("sp_na.dat")

plt.clf()
plt.plot(dat[:,0],dat[:,2],"o-",lw=2)
plt.xlabel("Rydberg Coupling")
plt.ylabel("Fidelity")
plt.tight_layout()
plt.title("SP Gate - Single Plaquette")
plt.tight_layout()
plt.xscale("log")
plt.savefig("sp_single_plaquette.png",dpi=300)
plt.savefig("sp_single_plaquette.eps")


plt.clf()
plt.plot(dat[:,0],dat[:,1],"o-",lw=2)
plt.xlabel("Rydberg Coupling")
plt.ylabel("Fidelity")
plt.tight_layout()
plt.title("Single SP Gate")
plt.tight_layout()
plt.xscale("log")
plt.savefig("sp_two_atoms.png",dpi=300)
plt.savefig("sp_two_atoms.eps")



plt.clf()
plt.plot(dat[:,0],dat[:,1],"o-",lw=2,label="Single Gate")
plt.plot(dat[:,0],dat[:,2],"o-",lw=2,label="Plaquette")
plt.xlabel("Rydberg Coupling")
plt.ylabel("Fidelity")
plt.title("SP Gate")
plt.legend()
plt.tight_layout()
plt.xscale("log")
plt.savefig("sp_gate_and_plaquette.png",dpi=300)
plt.savefig("sp_gate_and_plaquette.eps")



