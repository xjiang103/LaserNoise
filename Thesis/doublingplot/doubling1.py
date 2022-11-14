import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
pts = np.array([[2,2], [4,4], [10,4],[12,2]])
p = Polygon(pts, closed=True,color="black",fill=False,linewidth=3)
ax = plt.gca()
ax.add_patch(p)
ax.set_xlim(1,14.2)
ax.set_ylim(1,14.2)
plt.show()
