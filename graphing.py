import matplotlib.pyplot as plt
import sys
import json
import re

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

    plt.plot()
    
