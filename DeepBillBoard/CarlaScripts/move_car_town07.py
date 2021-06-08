import carla

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

