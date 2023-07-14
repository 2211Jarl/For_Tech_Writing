import tflearn
from tflearn.datasets import mnist

x_train, y_train, x_test, y_test=mnist.load_data(one_hot=True)

print("Training Data shape: ", x_train.shape)
print("Training Labels shape: ", y_train.shape)
print("Testing Data shape: ", x_train.shape)
print("Testing Labels shape: ", y_train.shape)

print("First 5 training labels: ")
print(y_train[:5])

i_layer=tflearn.input_data(shape=[None,784])
h_layer=tflearn.fully_connected(i_layer, 256, activation='relu')
o_layer=tflearn.fully_connected(h_layer, 10, activation='softmax')
net=tflearn.regression(o_layer, optimizer='adam', learning_rate=0.1, 
                       loss='categorical_crossentropy')

model=tflearn.DNN(net)
model.fit(x_train, y_train, validation_set=(x_test,y_test),
          n_epoch=20, batch_size=128)

acc=model.evaluate(x_test,y_test)
print("Accuracy: ", acc)