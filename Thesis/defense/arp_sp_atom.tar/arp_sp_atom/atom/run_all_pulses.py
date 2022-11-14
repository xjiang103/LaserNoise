import subprocess
import numpy as np
import argparse

dat_num = 0
parser = argparse.ArgumentParser()
parser.add_argument('-i','--dat_num',type=int)
args = vars(parser.parse_args())
if args["dat_num"] is not None:
    dat_num = args["dat_num"]

data = np.loadtxt("na_sp2_op.dat")

dat = data[dat_num]
b = dat[0]
p0 = dat[1]
p1 = dat[2]
fid2 = dat[3]
delta  = dat[4]
deltat = dat[5]

fid5 = float(subprocess.check_output(["./na_5_seq_3lvl2","-ts_rk_type","5bs","-ts_rtol","1e-8","-ts_atol","1e-8","-n_ens","-1",
                                     "-pulse_type","SP",
                                     "-b_term",str(b),
                                     "-delta",str(delta),
                                     "-deltat",str(deltat),
                                     "-phase_qb0",str(p1), #p1 and p0 are correct - qutip and quac have different ordering
                                     "-phase_qb1",str(p0)]).split()[-1]) #the way we coded it

print(b,fid2,fid5)
