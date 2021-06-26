import carla
import time
import os
import shutil
from math import cos,sin

index = 0
directory_name = "output/"

'''
This function will be called asynchronously
It takes as input the image captured by the rgb camera attached to the vehicle and saves it into a directory associated with an index
'''
def save_data(image):
	global index
	global directory_name
	if index > 2:
		image.save_to_disk(directory_name + str(index-3) + 'th_img.png')
	index = index + 1

'''
Here we connect our client to Carla on port 2000
We get the world variable that contains every object instantiated
After this we recover all the actors in our scene
'''
client = carla.Client('localhost', 2000)
world = client.get_world()
actors_list = world.get_actors()


'''
We prepare the view and the position of the camera in order to attach it to the vehicle and hide its hood
'''
location = carla.Location(0, 0, 0)
rotation = carla.Rotation(20, 0, 0)
transform = carla.Transform(location, rotation)

'''
We recover the vehicle created by OpenPilot in order to attach to it our rgb camera
'''
counter = 0
for i in actors_list:
	if i.type_id == "sensor.camera.rgb":
		if counter == 0:
			cam_transform = i.get_transform()
			vehicle = i
		counter += 1

'''
If the output directory exists we delete it in order to save newer images
'''
if os.path.exists(directory_name):
        shutil.rmtree(directory_name)

'''
If the camera does not exist already we create it and launch the capture
'''
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

'''
We need to make the program continue until we have enough franes captured by our camera
We could either end the program manually we have enough frames or reduce the time before the programs end
'''
time.sleep(80)

