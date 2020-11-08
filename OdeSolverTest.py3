# Python ODE Solver Test - Scipy
import numpy as np
import math
from scipy.integrate import odeint
import matplotlib.pyplot as plt

dmdt = 6.; #kg/s
ve = 50.; #m/s
m0 = 40.; #kg
pe = 20 * 10300.; #pa
po = 10300.; #pa
ae = 0.005; #m^2
cd = 0.4;
tho = 1.225; #kg/m^3
a = 0.01; #m^2
theta = math.pi / 2;
g = 9.8; #km/s^2

def dv_dt(v,t):
	dvdt = dmdt*ve/(m0-dmdt*t) + (pe-po)*ae/(m0-dmdt*t) - cd*tho*(np.power(v,2))*a/(2*(m0-dmdt*t)) - g*math.sin(theta);
	return dvdt;

ts = np.linspace(0,5,10000);
v0 = 0;
v = odeint(dv_dt,v0,ts);

# plt.plot(ts,v);
# plt.show();

# plt.figure();

gap = 0.001;
x = np.zeros(len(ts));

for i in range(len(ts)-1):
	dx = gap * v[i];
	x[i+1] = x[i] + dx;

# plt.plot(ts,x);
# plt.show();