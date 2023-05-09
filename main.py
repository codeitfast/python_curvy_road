from math import sqrt, atan
import os
from typing import Dict
import matplotlib.pyplot as plt


cwd = os.getcwd()
files = os.listdir(cwd)

allRoads = {}

print('roads: ')
for i in files:
    print('   - ', i)
printRoad = input('road for matplotlib (just name, not *.csv): ')

def smooth(n, y):
    #n = distance to blur/smooth, y is an array of the original points
    new = []
    for i in range(len(y)):
        total = 0
        added = 0
        for j in range(n, -n, -1):
            try:
                total += y[i + j]
                added += 1
            except:
                pass
        total /= (added)
        new.append(total)
    return new

for fileName in files:

    if(fileName == "main.py"):
        continue
    #fileName = input('file name (q to exit): ')
    #if(fileName.lower() == 'q'):
    #    break
    file = open(fileName)
    nx = []
    ny = []


    #get x & y
    for i in file:
        nx.append(float(i.split(',')[0].strip()))
        ny.append(float(i.split(',')[1].strip()))

    try:
        x = smooth(3,nx)
        y = smooth(3,ny)
        x = x[2:]
        y = y[2:]
    except:
        x = nx
        y = ny

    if(fileName==printRoad + ".csv"):
        fig, ax = plt.subplots()
        ax.plot(nx,ny, c="#ff00ff")
        ax.plot(x,y, c="#151515")
        #add legend
        plt.show()

    ds = []
    dtheta = []
    for i, n in enumerate(x):
        if(i != len(x) - 1):
            ds.append(sqrt((x[i + 1] - x[i])**2 + (y[i + 1] - y[i])**2))
        if(i < len(x) - 2):
            dtheta.append(atan(
                (y[i + 2] - y[i + 1])/(x[i+2] - x[i + 1] + 10**-100)
            ) - atan(
                (y[i + 1] - y[i])/(x[i+1] - x[i] + 10**-100)
            ))

    kappa = []
    for i, n in enumerate(dtheta):
        kappa.append(abs(n/ds[i]))

    average = 0
    for i in kappa:
        average += i
    average /= len(kappa)
    average /= 346000
    average = 1/average

    allRoads[fileName] = average


'''def print_dict(data: Dict[str, float]) -> None:
    sorted_keys = []
    sorted_values = [value for value in sorted(data.values(), reverse=False)]
    sorted_keys = [str(key) for key in sorted(data.keys(), reverse=True)]
    sorted_dict = {k: v for k, v in zip(sorted_keys, sorted_values)}
    
    for i in range(len(sorted_keys)):
        print(str(sorted_keys[i]) + ' ---> ' + str(round(sorted_values[i], 4)))
    
print(print_dict(allRoads))'''
for i in {k: v for k, v in sorted(allRoads.items(), key=lambda item: item[1])}:
    print(i + ' ---> ' + str(allRoads[i]))
