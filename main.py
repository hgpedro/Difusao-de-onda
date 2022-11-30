import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def r_t0(x):
  sigma = 0.1
  ro = (np.exp((-x**2)/(2*(sigma**2))))/(sigma*np.sqrt(2*np.pi))
  return ro

delta_t = 0.0001
delta_x = np.sqrt(2*delta_t)
list_x = np.arange(-1, 1, delta_x)
list_r_t0 = []
for x in list_x:
  list_r_t0.append(r_t0(x))
list_r_t0[0] = 0
list_r_t0[-1] = 0
list_r = [list_r_t0]

k = 1

for n in range(500):
  list_proximo_ro = [0]
  for i in range(1, len(list_x)-1):
    proximo_ro = list_r[n][i] + (1/k) * delta_t * ((list_r[n][i-1] - 2*list_r[n][i] + list_r[n][i+1]) / delta_x**2)
    list_proximo_ro.append(proximo_ro)
  list_proximo_ro.append(0)
  list_r.append(list_proximo_ro)

fig = plt.figure()
ax0 = plt.axes(xlim=(-1,1), ylim=(0,4))

line, = ax0.plot(list_x, list_r[n])

def animation_function(n):
  x = list_x
  y = list_r[n]
  line.set_data(x, y)
  return line,

anim = FuncAnimation(fig, func=animation_function, frames=500, interval=20, blit=True)
plt.show()

list_alarg = []
for ro in list_r:
  list_alarg.append(np.std(ro))
list_t = np.arange(501)
list_t2 = np.arange(501)**2
list_t3 = np.arange(501)**3

list_raiz_t = np.sqrt(np.arange(501))
list_raiz3_t = np.arange(501)**(1/3)

plt.plot(list_t, list_alarg)
plt.title("t")
plt.show()
plt.plot(list_t2, list_alarg)
plt.title("t ao quadrado")
plt.show()
plt.plot(list_t3, list_alarg)
plt.title("t ao cubo")
plt.show()
plt.plot(list_raiz_t, list_alarg)
plt.title("raiz de t")
plt.show()
plt.plot(list_raiz3_t, list_alarg)
plt.title("raiz cúbica de t")
plt.show()

def y_0(x, x_c=0.3, k=1000):
  y = np.exp(-k*(x-x_c)**2)
  return y

c = 50
delta_t = 0.0001
delta_x = c*delta_t
list_x = np.arange(0, 1, delta_x)
list_y_0 = list(map(y_0, list_x))
list_y_0[0] = 0
list_y_0[-1] = 0
list_y = [list_y_0,list_y_0]
p = 1

for n in range(1, 100):
  list_next_y = [0]
  for i in range(1, len(list_x)-1):
    proximo_y = (2*(1-(p**2)) * list_y[n][i]) + ((p**2) * (list_y[n][i+1] + list_y[n][i-1]) - list_y[n-1][i])
    list_next_y.append(proximo_y)
  list_next_y.append(0)
  list_y.append(list_next_y)

fig = plt.figure()
ax = plt.axes(xlim=(0,1), ylim=(0,2))
line, = ax.plot(list_x, list_y[0])

def animation_function(n): 
  x = list_x
  y = list_y[n]
  line.set_data(x, y)
  return line,

anim = FuncAnimation(fig, func=animation_function, frames=101, interval=20, blit=True)
plt.show()