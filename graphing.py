import matplotlib.pyplot as plt
import sys
import json
import re
import numpy as np

#def plot(x_axis, y_axis):


if __name__ == '__main__':
    lst = sys.argv[1:]
    x = []
    y = []
    x_insert = False
    y_insert = False
    for i in lst:

        if '[' in i and len(x) == 0:
            i = re.sub('[,\[\]]', '', i)
            x.append(int(i))
            x_insert = True
            continue

        elif '[' in i and len(x) > 0:
            i = re.sub('[,\[\]]', '', i)
            y.append(int(i))
            x_insert = False
            y_insert = True
            continue

        if x_insert == True:
            i = re.sub('[,\[\]]', '', i)
            x.append(int(i))

        elif y_insert == True:
            i = re.sub('[,\[\]]', '', i)
            y.append(int(i))

    t = []
    for i in range(len(x)):
    	t.append(i)


    x = np.array(x)
    y = np.array(y)
    t = np.array(t)

    plt.plot(t, x, 'b', label='x line')
    plt.plot(t, y, 'g', label='y line')
    plt.show()

