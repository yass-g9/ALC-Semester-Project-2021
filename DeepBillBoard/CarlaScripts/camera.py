import carla
import time
import os
import shutil
from math import cos,sin

index = 0
directory_name = "output/"

def save_data(image):
	global index
	global directory_name
	if index > 2:
		image.save_to_disk(directory_name + str(index-3) + 'th_img.png')
	index = index + 1

client = carla.Client('localhost', 2000)
world = client.get_world()
actors_list = world.get_actors()

location = carla.Location(0, 0, 0)
rotation = carla.Rotation(20, 0, 0)
transform = carla.Transform(location, rotation)


counter = 0
for i in actors_list:
	if i.type_id == "sensor.camera.rgb":
		if counter == 0:
			cam_transform = i.get_transform()
			vehicle = i
		counter += 1

if os.path.exists(directory_name):
        shutil.rmtree(directory_name)

if counter == 1:
	cam_bp = world.get_blueprint_library().find('sensor.camera.rgb')
	cam_bp.set_attribute("image_size_x",str(1920))
	cam_bp.set_attribute("image_size_y",str(1080))
	cam_bp.set_attribute("fov",str(90))
	ego_cam = world.spawn_actor(cam_bp, transform, vehicle)
	ego_cam.listen(lambda image: save_data(image))
else:
	counter = 0
	for i in actors_list:
		if i.type_id == "sensor.camera.rgb":
			if counter == 1:
				i.listen(lambda image: save_data(image))
			else:
				counter += 1

time.sleep(80)

