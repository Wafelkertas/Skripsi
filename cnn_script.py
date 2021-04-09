import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator


base_dir = 'D:\projectmachinelearning\Skripsi\images'

edible_dir = os.path.join(base_dir, 'Edible')
inedible_dir = os.path.join(base_dir, 'Inedible')
poisonous_dir = os.path.join(base_dir, 'Poisonous')

model = tf.keras.models.Sequential([
	tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(150,150,3)),
	tf.keras.layers.MaxPooling2D(2,2),
	tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
	tf.keras.layers.MaxPooling2D(2,2),
	tf.keras.layers.Conv2D(128, (3,3), activation='relu'),
	tf.keras.layers.MaxPooling2D(2,2),
	tf.keras.layers.Conv2D(128, (3,3), activation='relu'),
	tf.keras.layers.MaxPooling2D(2,2),
	tf.keras.layers.Dropout(0.5),
	tf.keras.layers.Flatten(),
	tf.keras.layers.Dense(512, activation='relu'),
	tf.keras.layers.Dense(1, activation='sigmoid')
	])

model.compile(optimizer='adam',
	loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True), 	
	metrics=['accuracy'])


train_datagen = ImageDataGenerator(
	rescale=1./255,
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest',
    validation_split=0.2
    )

train_generator = train_datagen.flow_from_directory(
	base_dir,
	target_size=(150, 150),
	batch_size=20,	
	class_mode='sparse',
	subset="training"
	)

validation_generator = train_datagen.flow_from_directory(
	base_dir,
	target_size=(150,150),
	batch_size=20,	
	class_mode='sparse',
	subset="validation"
	)

history = model.fit(
	train_generator,
	steps_per_epoch=100,
	epochs=100,
	validation_data=validation_generator,
	validation_steps=50,
	verbose=2)


