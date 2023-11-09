import numpy as np
h=100
a=np.pi/3
b=30
g= 9.807
v=(((g*h*((np.tan(b))**2))/((2*(np.cos(a))**2)*(1-((np.tan(a))*(np.tan(b))))))**1/2)

s=(g*h)*((np.tan(b))**2)
k= (2 * ((np.cos(a))**2))
j = 1 - ((np.tan(b))*(np.tan(a)))

r=(s/(k*j))**(1/2)

print(r)