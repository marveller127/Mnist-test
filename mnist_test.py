import tensorflow.examples.tutorials.mnist.input_data as input_data
mnist=input_data.read_data_sets('Mnist_data/',one_hot=True)
import tensorflow as tf
sess=tf.InteractiveSession()
x=tf.placeholder('float',shape=[None,784])
y_=tf.placeholder('float',shape=[None,10])
w=tf.Variable(tf.zeros([784,10]))
b=tf.Variable(tf.zeros([10]))
sess.run(tf.initialize_all_variables())
y=tf.nn.softmax(tf.matmul(x,w)+b)
cross_entropy=-tf.reduce_sum(y_*tf.log(y))
train_step=tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)
for i in range(1000):
    batch=mnist.train.next_batch(50)
    train_step.run(feed_dict={x:batch[0],y_:batch[1]})
correct=tf.equal(tf.argmax(y,1),tf.argmax(y_,1))
accuracy=tf.reduce_mean(tf.cast(correct,'float'))
print('----- this is the end of program and accurary is ------\n{}'.format(1))
print(accuracy.eval(feed_dict={x:mnist.test.images,y_:mnist.test.labels}))
