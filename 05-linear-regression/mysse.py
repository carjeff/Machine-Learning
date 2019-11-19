import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from sse import loss
import matplotlib.pyplot as plt

import numpy as np
from sklearn.datasets import make_regression
rx, ry = make_regression(
    n_samples=100,
    n_features=1,
    noise=1,
    bias=1
)

w0 = np.linspace(-10,10,100)
w1 = np.linspace(-10,10,100)
errors = []
for w,n in zip(w0,w1):
    errors.append(loss(rx,ry,[w,n]))
error = np.array(errors)
_w0,_w1 = np.meshgrid(w0,w1)
fig = plt.figure(figsize=(10, 10))
ax = fig.gca(projection='3d')
ax.plot_surface(X=_w0,Y=_w1,Z=error)
plt.show()