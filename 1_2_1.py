from numpy import linspace
from scipy.integrate import solve_ivp

grv_const = 9.81
init_pos = 0
init_vel = 0.5
init_mass = 5

init_cond = [init_pos, init_vel, init_mass]

init_time = 0
final_time = 5
num_data = 100

tout = linspace(init_time, final_time, num_data)

def free_falling_obj(time, state, grv_const):
    x1, x2, x3 = state
    dxdt = [x2,
            grv_const + (x3-2)*(x2/x3),
            -x3+2]
    return dxdt


sol = solve_ivp(free_falling_obj, (init_time, final_time), init_cond, t_eval=tout, 
                args=(grv_const,))

xout = sol.y

print('df')


import matplotlib.pyplot as plt

plt.figure(1, figsize=(3,3))
plt.plot(tout, xout[0, :])
plt.xlabel('time, s')
plt.ylabel('position, m')


plt.figure(2)
plt.plot(tout, xout[1, :])
plt.xlabel('velocity, m/s')
plt.ylabel('position, m')
plt.axis([0, 10, 0, 0.5])

plt.figure(3)
plt.plot(tout, xout[2, :])
plt.xlabel('mass, kg')
plt.ylabel('position, m')

plt.show()