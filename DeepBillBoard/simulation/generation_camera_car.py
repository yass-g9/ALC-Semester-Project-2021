'''
This script generates the car and the camera at a specific position to run the simulation
'''
import carla


'''
We connect the client to Carla on port 2000
The we get the world and all its actors.
'''
client = carla.Client('localhost', 2000)
world = client.get_world()
actors_list = world.get_actors()

'''
We chose the rotation of the camera and the car and we select the pace of the car
'''
rotation_car = carla.Rotation(0, 0, 0)
velocity = carla.Vector3D(3, 0, 0)
angular_velocity = carla.Vector3D(0, 0, 0)
rotation_camera = carla.Rotation(20, 0, 0)

'''
We get the blueprint to create our car if needed and initialize our angle to 0 (steers in the middle)
'''
no_vehicle = True
blueprint_library = world.get_blueprint_library()
actors_list = world.get_actors()
control = carla.VehicleControl()
control.steer = 0

'''
Here we create the car and the camera if they are not created
We put move the car and the camera attached to the road
'''
for i in actors_list:
	if i.type_id == "vehicle.tesla.model3":
		actor = i
		location_car = actor.get_location()
		location_car.x = 190
		location_car.y = 133.5
		actor.apply_control(control)
		transform_car = carla.Transform(location_car, rotation_car)
		actor.set_transform(transform_car)
		no_vehicle = False
if (no_vehicle):
	blueprint = blueprint_library.find('vehicle.tesla.model3')
	location_car = carla.Location(190, 133.5, 2)
	transform_car = carla.Transform(location_car, rotation_car)
	actor = world.spawn_actor(blueprint, transform_car)
	actor.apply_control(control)
	cam_bp = world.get_blueprint_library().find('sensor.camera.rgb')
	cam_bp.set_attribute("image_size_x",str(1920))
	cam_bp.set_attribute("image_size_y",str(1080))
	cam_bp.set_attribute("fov",str(90))
	transform_camera = carla.Transform(carla.Location(0, 0, 2), rotation_camera)
	ego_cam = world.spawn_actor(cam_bp, transform_camera, actor)
    
'''
We apply the pace of the car here
'''
actor.set_target_velocity(velocity)


