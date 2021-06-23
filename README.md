# ALC-Semester-Project-2021

## How to install Unreal Engine 4.24 on Linux

#### Register into Epic Games

You will find the Github repository of [Unreal Engine](https://github.com/EpicGames/UnrealEngine) source code. However, this repository was made private by Epic Games so you first need to login or register freely to [Epic Games](https://www.epicgames.com/id/login) and connect your GitHub account in the [Connected Account Dashboard](https://www.epicgames.com/account/connections#accounts) of Epic Games. Then, go on the GitHub of [Epic Games](https://github.com/EpicGames) and accept the invitation from Epic Games. You should now see the Unreal Engine repository.

#### Building Unreal Engine 4.24

Now that you have access to the GitHub repository, you must choose the ```4.24``` branch and clone it. 

Then, go into the cloned folder and build it by launching the following command line.
```bash
./Setup.sh && ./GenerateProjectFiles.sh && make
```

## Run Carla 0.9.11 with Unreal Engine 0.4.24

#### Get assets

You first need to clone the [Carla GitHub](https://github.com/carla-simulator/carla). Once this is done, run the following command line to to get the latest assets that will be .
```bash
./Update.sh
```

#### Set Unreal Engine environment variable

Then, we will have to set the Unreal Engine environment variable. To do it persistently across sessions, open one of those two files.
```bash
gedit ~/.bashrc
# or
gedit ~/.profile
```

Then, add the following line to the bottom of the file.
```bash
make launch
```

Then run the following command line to start Carla with Unreal Engine.
```bash
export UE4_ROOT=~/UnrealEngine_4.24
```

Save the file and restart the terminal. 

#### Build Carla on Unreal Engine

We first need to compile the Python API clinet that will grant control over the simulation.
```bash
make PythonAPI
```

Then to open Carla on Unreal Engine editor, run the following command line.
```bash
make launch
```

To start the server simulation, press the ```Play``` button in Unreal Engine editor.
