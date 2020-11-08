import numpy as np
import math
from scipy.integrate import odeint
import matplotlib.pyplot as plt

k = 1;

def dv_dt(v,t):
	dvdt = k*v;
	return dvdt;

ts = np.linspace(0,5,1000);
v0 = 1;
v = odeint(dv_dt, v0, ts);

plt.plot(ts,v);
plt.show();