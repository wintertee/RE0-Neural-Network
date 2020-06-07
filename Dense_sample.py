from Re0_neural_network import activations, initializers, layers, losses, models, optimizers

import numpy as np
import matplotlib.pyplot as plt

# load dataset
mnist = np.load('datasets/mnist.npz')
train_images = mnist['train_images']
train_labels = mnist['train_labels']
test_images = mnist['test_images']
test_labels = mnist['test_labels']

# flatten image
train_images = train_images.reshape(60000, 784, 1).astype(float)
# normalisation
train_images /= 255

# one-hot encode
targets = train_labels.reshape(-1)
train_labels = np.eye(10)[targets].reshape(60000, 10, 1)

model = models.Sequential()
model.append(layers.Dense(784, 64, activations.relu, initializers.He))
model.append(layers.Dense(64, 10, activations.softmax, initializers.He))
model.build()

model.config(optimizer=optimizers.SGD, loss=losses.Crossentropy, lr=0.001, batch_size=20)
# model.config(optimizer=optimizers.PRBCD, loss=losses.Crossentropy, lr=0.001)
# model.config(optimizer=optimizers.RCD, loss=losses.Crossentropy, lr=0.001, n=10000)

losses = []
for epoch in range(6):
    loss = model.fit(train_images, train_labels, 0.001)
    loss = np.mean(loss)
    losses.append(loss)
    print("epoch: " + str(epoch + 1) + " loss: " + str(loss))

epochs = range(1, len(losses) + 1)

plt.plot(epochs, losses, label='loss')
plt.show()
