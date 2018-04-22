'''
Exploring some of the examples in this article... 
https://www.kdnuggets.com/2017/05/how-not-program-tensorflow-graph.html
'''

import numpy as np
import tensorflow as tf
 
session = tf.Session()
initializer = tf.global_variables_initializer()
session.run(initializer)

print("some numpy array exercises")
print("create a 2x2 array, with each element initialized to a value of 1.0")
x = np.ones((2,2))
print(x)

print ("Use numpy .sum() on the contents of the array")
print (x.sum())


print("Use to TensorFlow .reduce_sum() on the contents of the array")
y = session.run(tf.reduce_sum(x))
print(y)


