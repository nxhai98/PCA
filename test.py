import numpy as np
from numpy import loadtxt
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

data = loadtxt('data.csv', delimiter=',', dtype=np.complex_)
vector = loadtxt('vector.csv', delimiter=',', dtype=np.complex_)

path = []


N, n = data.shape


f = open('path_arr.txt', 'r+')
for i in range(0, N):
    try:
        line = f.readline()
        path.append(line[:-1])
    except:
        print("some thing failed")

print(path)

def get_distance(image_num):
    distance = []
    for i in range(0, N):
        temp = np.linalg.norm(data[image_num] - data[i])
        distance.append(temp)
    return distance


dist = get_distance(4)
dist = np.array(dist)
print(dist)
result = np.argsort(dist)
for i in range(0, 10):
    img = mpimg.imread(path[result[i]])
    plt.figure()
    imgplot = plt.imshow(img);
    plt.show()
print(result)
