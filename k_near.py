# basic function
import numpy as np
def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]

array = np.random.random(10)
print(array)


value = 0.5

print(find_nearest(array, value))
"""
output
[0.75198416 0.49174073 0.60859666 0.76247672 0.23566381 0.58289662
 0.17482078 0.25150263 0.74023751 0.7711735 ]
0.49174072866221197

"""
#using KDTree
 # Create some dummy data
y_array = numpy.random.random(10000).reshape(100,100)
x_array = numpy.random.random(10000).reshape(100,100)
points = numpy.random.random(10000).reshape(2,5000)


combined_x_y_arrays = numpy.dstack([y_array.ravel(),x_array.ravel()])[0]
points_list = list(points.transpose())


def do_kdtree(combined_x_y_arrays,points):
    mytree = scipy.spatial.cKDTree(combined_x_y_arrays)
    dist, indexes = mytree.query(points)
    return indexes

start = time.time()
results2 = do_kdtree(combined_x_y_arrays,points_list)
end = time.time()
print(results2)
print ('Completed in: ',end-start)

"""
output
[2636 3797 4969 ... 7343 7604 1942]
Completed in:  0.013770341873168945

"""
# find nearest
import numpy as np
def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]

array = [-1.1171317 , -1.8356392 ,  1.0730016 , -1.479594  ,  0.7007265 ,
       -0.42651197,  1.9171674 , -0.17966518, -0.45103863, -1.2271085 ,
       -0.5789978 , -0.4186229 ,  0.2492581 ]
print(array)


value = [-0.47695143, -1.43616823,  1.03467011, -1.32564479,  0.70711739,
       -0.34028656,  1.91669133, -0.14321669,  3.87500921, -1.70714343,
       -0.17066299,  0.03404049,  0.24368604]

print(find_nearest(array, value))

"""
output
-1.1171317, -1.8356392, 1.0730016, -1.479594, 0.7007265, -0.42651197, 1.9171674, -0.17966518, -0.45103863, -1.2271085, -0.5789978, -0.4186229, 0.2492581]
1.9171674
"""
from sklearn.neighbors import NearestNeighbors
import numpy as np
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
nbrs = NearestNeighbors(n_neighbors=2, algorithm='ball_tree').fit(X)
distances, indices = nbrs.kneighbors(X)
print("indices- ", indices)
print("distances- ", distances)
#Because the query set matches the training set,
#the nearest neighbor of each point is the point itself, 
# at a distance of zero.
"""
indices-  [[0 1]
 [1 0]
 [2 1]
 [3 4]
 [4 3]
 [5 4]]
distances-  [[0.         1.        ]
 [0.         1.        ]
 [0.         1.41421356]
 [0.         1.        ]
 [0.         1.        ]
 [0.         1.41421356]]


"""







