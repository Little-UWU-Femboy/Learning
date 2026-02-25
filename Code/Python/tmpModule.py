import numpy as np

x = np.arange(5)

print(x)

x = x[np.newaxis, :]
x = x[:, np.newaxis]

# x[0][0]=30

print(x.shape)

print(x)
