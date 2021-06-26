import carla

'''
This program moves the car created by OpenPilot to another road (here it is for town 07) since the spawn points have changed when we added our billboard
We connect our client to Carla on port 2000
We get the world and its actors and move the actor if it is the tesla model created by OpenPilot to a position we selected
'''

client = carla.Client('localhost', 2000)
world = client.get_world()
actors_list = world.get_actors()
location = carla.Location(-40, 56, 1)
rotation = carla.Rotation(0, 180, 0)

transform = carla.Transform(location, rotation)

for i in actors_list:
	if i.type_id == "vehicle.tesla.model3":
		print(i)
		i.set_transform(transform)

