import math
from matplotlib import pyplot as plt
import numpy as np

t = np.linspace(0,1,10000) #time points, 10,000 of them, between 0 and 1 second

class Signal():
    def __init__(self,t):
        self.t = t
    
    def f(self):
        return 3*(np.cos(2*np.pi*t)) + 12*(np.cos(2*np.pi*2*t)) - 0.8*(np.sin(2*np.pi*3*t)) + 15*(np.cos(2*np.pi*t*5)) + 100*(np.sin(2*np.pi*7*t))
    
signal = Signal(t)
f = signal.f()

comps = []
magnitudes = []
for n in range(1,11):
    probe = np.exp(-2j * np.pi * n * t)
    c = np.trapezoid(f * probe, t)*2
    m = np.sqrt(c.real**2 + c.imag**2) #np.abs(c)
    magnitudes.append(float(m))
    comps.append(c)

print(comps)

plt.stem(range(1, 11), magnitudes)
plt.title('Magnitude of Fourier Coefficients')
plt.xlabel('Frequency (n)')
plt.ylabel('Magnitude')
plt.xticks(range(1, 11))
plt.tight_layout()
plt.show()

