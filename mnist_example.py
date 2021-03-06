from model_elm import ELM
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# Basic tf setting
tf.set_random_seed(2016)
sess = tf.Session()

# Get data
mnist = input_data.read_data_sets("/tmp/data/", one_hot=True)

# Construct ELM
batch_size = 5000
hidden_num = 150
print("batch_size : {}".format(batch_size))
print("hidden_num : {}".format(hidden_num))
elm = ELM(sess, batch_size, 784, hidden_num, 10)

# one-step feed-forward training
train_x, train_y = mnist.train.next_batch(batch_size)

print('train_x shape : ', train_x.shape)
print('train_y shape : ', train_y.shape)
elm.feed(train_x, train_y)

# testing
elm.test(mnist.test.images, mnist.test.labels)