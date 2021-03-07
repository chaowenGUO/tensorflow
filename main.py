import tensorflow
tpu = tensorflow.distribute.cluster_resolver.TPUClusterResolver()
tensorflow.config.experimental_connect_to_cluster(tpu)
tensorflow.tpu.experimental.initialize_tpu_system(tpu)
tpu_strategy = tensorflow.distribute.experimental.TPUStrategy(tpu)
mnist = tensorflow.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255, x_test / 255
model = tensorflow.keras.models.Sequential([tensorflow.keras.layers.Flatten(input_shape=(28, 28)), tensorflow.keras.layers.Dense(128, activation='relu'), tensorflow.keras.layers.Dropout(0.2), tensorflow.keras.layers.Dense(10, activation='softmax')])
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=5)
model.save('model')
model.evaluate(x_test, y_test, verbose=2)
