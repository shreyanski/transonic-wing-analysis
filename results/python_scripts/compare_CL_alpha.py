import numpy as np 
import matplotlib.pyplot as plt

#"simulations/xflr5/VLM_H10K_V158_C143.txt"
# data = np.loadtxt(file_HALE, skiprows=8)
# [alpha, CL_xflr5, CDi_xflr5] = [data[:,0], data[:,2], data[:,3]]
# could also use pandas instead (recommended)

# CLa - XFLR5 VORTEX-LATTICE METHOD
file_HALE = "simulations/xflr5/baseline_wing_CL_alpha_curve.txt"
alpha, CL_xflr5 = np.loadtxt(file_HALE, skiprows=1, usecols=(0,1), unpack=True)

# CLa - PRANDTL LLT THEORETICAL CORRECTION
b = 40
S = 54.4
AR = 29.412 #b**2 / S
e = 0.991
a0 = 2*np.pi
a = a0 / (1 + a0/np.pi/e/AR)
CL_llt = a * np.radians(alpha)

# Plotting the lift-polars
plt.plot(alpha, CL_llt, 'x-', label='LLT 3D corrected')
plt.plot(alpha, CL_xflr5, 'o-', label='XFLR5')
plt.title('XFLR5 vs classical theory - 3D wing')
plt.xlabel(r'Angle of attack, $\alpha$')
plt.ylabel('Lift coefficient, $C_L$')
plt.grid(visible=True, which='major')
plt.legend()
plt.savefig('results/figures/lift_polar_comparison.png')

# COMMENT ON RESULTS
# XLFR5 overpredicts lift (and underpredicts drag)? Separation effects aren't considered, but are they relevant at this flight regime (Re=2e6 and Ma=0.47). The lift curve slopes are the same however and for jet-powered UAVs like these, is worth extracting from this low-fidelity simulation.





