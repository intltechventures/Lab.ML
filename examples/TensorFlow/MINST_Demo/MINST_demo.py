# References:
#	https://www.tensorflow.org/beta/
# 	https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/r2/tutorials/quickstart/beginner.ipynb#scrollTo=0trJmd6DjqBZ 

from __future__ import absolute_import, division, print_function, unicode_literals

import tensorflow as tf

# Load and prepare the MNIST dataset. Convert the samples from integers to floating-point numbers:
mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0


# Build the tf.keras.Sequential model by stacking layers. Choose an optimizer and loss function for training:

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
			  
			  
# Train and evaluate the model:

model.fit(x_train, y_train, epochs=5)

model.evaluate(x_test, y_test)


# The image classifier is now trained to ~98% accuracy on this dataset. 			  

