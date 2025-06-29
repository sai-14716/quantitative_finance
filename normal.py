import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

variables = []
variables.append(10)
variables.append(12)
variables.append(20000)

a = np.random.normal(variables[0], variables[1], variables[2])

plt.xlabel("n")
plt.ylabel("outcome")
plt.plot(a)
plt.show()

#Converting outcomes to the probability

m = int(a.min())
pdf = np.zeros(int(a.max())-int(a.min())+1)

for i in a:
    pdf[int(i)+m+1] += 1

print(pdf.sum())

plt.xlabel("Range")
plt.ylabel("Probability")
plt.plot(pdf)
plt.xlim(variables[0]-variables[1],variables[0]+variables[1])
plt.show()
