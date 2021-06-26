import carla
import time
import os
import shutil
import glob
from pathlib import Path

from os.path import basename
from PIL import ImageFile
from driving_models import *
from math import pi

client = carla.Client('localhost', 2000)
world = client.get_world()
actors_list = world.get_actors()

directory_name = "output/"
counter = 0

shutil.rmtree('./output')
os.mkdir('./output')

def save_data(image):
	global counter
	global directory_name
	#time.sleep(1)
	image.save_to_disk(directory_name + 'img_' + str("%03d" % counter) + '.png')
	print('Image ' + str(counter))
	counter += 1
	

def camera_save():
	for i in actors_list:
		if i.type_id == "sensor.camera.rgb":
			i.listen(lambda image: save_data(image))

def steer_car():
	ImageFile.LOAD_TRUNCATED_IMAGES = True
	os.environ["CUDA_VISIBLE_DEVICES"] = "0"
	img_rows, img_cols = 100, 100
	input_shape = (img_rows, img_cols, 3)
	input_tensor = Input(shape=input_shape)
	K.set_learning_phase(0)
	model1 = Dave_orig(input_tensor=input_tensor, load_weights=True)
	for i in actors_list:
		if i.type_id == "vehicle.tesla.model3":
			actor = i
	control = carla.VehicleControl()
	try:
		paths = sorted(Path('output').iterdir(), key=os.path.getmtime)
		print('Image used: ' + str(paths[-2]))
		filelist = glob.glob(os.path.join("output", '*.png'))
		control.steer = -(model1.predict(preprocess_image(paths[-2]))[0][0])/(5*pi)
		actor.apply_control(control)
		print("Angle applied :" + str(control.steer))
	except:
		print("Error reading file")


def main():
	time.sleep(2)
	camera_save()
	while True:
		steer_car()

main()

