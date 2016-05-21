import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import norm
from scipy.integrate import odeint
from matplotlib import animation

m, k, l = [1, 10, 10]
g = [0,-9.81]
x1=[0,0]
x2=[-l,0]
u1=[0,50]
u2=[-30,30]
t_k = 10
n = 500
nFrames = 300

def equation(Y, t):

    x1 = Y[:2]
    a1 = Y[2:4]
    x2 = Y[4:6]
    a2 = Y[6:8]

    dr = x2 - x1
    dY = np.zeros(8)

    if x1[1]<0 or x2[1]<0:
        return dY

    dY[2:4] = dr * k / m * (1 - l / norm(dr))
    dY[3] -= 9.81

    dY[6:] = -dr * k / m * (1 - l / norm(dr))
    dY[7] -= 9.81

    dY[:2] = a1
    dY[4:6] = a2

    return dY

Y0 = np.array([x1,u1,x2,u2]).reshape(8)   #mamy "w linii"
Y=odeint(equation, Y0, np.linspace(0, t_k, n))

fig=plt.figure()

plt.plot(Y[:,0], Y[:,1])
plt.plot(Y[:,4], Y[:,5])
p1, = plt.plot(Y0[0],Y0[1], '.', markersize=15, color="blue")
p2, = plt.plot(Y0[4],Y0[5], '.', markersize=15, color="blue")
spring, = plt.plot(Y0[4],Y0[5], '-', markersize=10, color="red")

plt.axes().set_aspect('equal', 'datalim')
plt.axes().grid(True)

def anim(frame):
    t = int(len(Y)*float(frame)/nFrames)                #czas
    x1 = Y[t, :2]
    x2 = Y[t, 4:6]

    p1.set_data(x1)
    p2.set_data(x2)
    spring.set_data([x1[0], x2[0]], [x1[1], x2[1]])

animacja = animation.FuncAnimation(fig, anim, frames=nFrames, interval=10, repeat=False)

plt.show()