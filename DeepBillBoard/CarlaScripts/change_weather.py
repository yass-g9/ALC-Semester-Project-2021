import carla

'''
This program just changes the weather in order to see if sunlight has an impact on our perturbation:
We connect our client to Carla on port 2000
We take all the world content from this client
After this we change the parameters of its weather and update it
'''
client = carla.Client('localhost', 2000)
world = client.get_world()
weather = world.get_weather()
weather.cloudiness = 50
weather.precipitation = 50
weather.sun_azimuth_angle = 270
world.set_weather(weather)
