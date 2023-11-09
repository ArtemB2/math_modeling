import numpy as np

h=6.62607015*(10**-34)
e=2.718
k=1.380649*(10**-23)
z=300
t=200
a=(2/((np.pi)**(1/2)))
b=(h/((k*t)**(3/2)))
c=(e**(-z/(k*t)))
d=(z**(t/2))

n=(a*b*c*d)

print(n)