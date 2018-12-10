import numpy as np
import matplotlib.pyplot as plt
r=np.random.RandomState(1)
x=10*r.rand(50)
y=x+r.randn(50)
plt.scatter(x,y)
dx=np.diff(x)
dy=np.diff(y)
m=dy.mean()/dx.mean()
plt.title('linear regression')
plt.xlabel('x')
plt.ylabel('y')
plt.scatter(x,y)
c=y.mean()-m*x.mean()
y1=m*x+c
plt.plot(x,y1)
plt.show()

