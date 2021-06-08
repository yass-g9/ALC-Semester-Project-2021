import carla

client = carla.Client('localhost', 2000)
world = client.get_world()
weather = world.get_weather()
weather.cloudiness = 50
weather.precipitation = 50
weather.sun_azimuth_angle = 270
world.set_weather(weather)
