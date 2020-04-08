import numpy as np
from numpy import array
from numpy import mean
from numpy import cov
from numpy.linalg import eig
from numpy import savetxt


# read pgm file
def read_pgm(pgmf):
    header = []
    header.append(pgmf.readline())
    (width, height) = [int(i) for i in pgmf.readline().split()]
    header.append([width, height])
    depth = int(pgmf.readline())
    header.append(depth)
    assert depth <= 255

    raster = []
    for y in range(height):
        row = []
        for y in range(width):
            row.append(ord(pgmf.read(1)))
        raster.append(row)
    return raster

def get_path(i):
    path = "train/" + str(i)+ ".pgm"
    return path

def read_data_set():
    data = []
    path_arr = []
    k = 0
    for i in range(1, 15):
        for j in range(1, 10):
            try:
                path = get_path(k)
                k += 1
                image_file = open(path, "rb")
                im = read_pgm(image_file)
                image_file.close()
                im = np.array(im)
                im = im.ravel()
                data.append(im)
                path_arr.append(path)
            except:
                print("Some thing went wrong")
    return data, path_arr

# data la ma tran 4k chieu doc tu hon 100 anh 64x64
data, path_arr = read_data_set()

savetxt('path_arr.txt', path_arr, delimiter=',', fmt='%s')

data = np.array(data)
# define a matrix
A = data
# calculate the mean of each column
M = mean(A.T, axis=1)
# center columns by subtracting column means
C = A - M
# calculate covariance matrix of centered matrix
V = cov(C.T)
# eigendecomposition of covariance matrix
values, vectors = eig(V)

# get 20 largest value
index = np.argsort(-1 * values)
index = index[0:20]
vectors = vectors.T
vectors = vectors[index, :]

# project data
P = vectors.dot(C.T)
print(P.T.shape)



savetxt('vector.csv', vectors, delimiter=',')

savetxt('data.csv', P.T, delimiter=',');



