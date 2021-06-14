# How to make a capture of differents frames in OpenPilot

## Requirements

* Carla 0.9.11
* Unreal Engine numero
* OpenPilot

## How to import the billboard into Carla

Once Carla and Unreal Engine have been well setup you can open Carla in the Unreal Engine Editor in order to add the Billboard.

```bash
cd carla
make launch
```

Once Unreal Engine Editor is open, you can select one of the town by going in the menu "File --> Open Level". Then you will need to import both appliances which are named "SmallBillboard.fbx" and "BigBillboard.fbx".

Then, you must go in the `DeepBillboard` folder to train a set of images in order to retrieve a perturbation that should make the car move to a direction.
```bash
cd code
python3.7 train.py -direction='right' -path='../Digital/digital_Dave_straight1'
```
`-direction` can be `'right'`' or `'left'`, which specifies the behavior of the adversarial direction result we want, `'left'` is in default.

`-path` is the digital case path, it can be modified to test different cases.

In the `train_output` folder, you will find a picture named as "20_new_logo.png" that will be the perturbation that we will use next.

Going back to Unreal Engine, you will need to import the perturbation you just got. Then, open the material 2 of the billboard and drag and drop the picture into it and linked it to the RGB of the Material 2.

Once that is done, you will just have to drag and drop the billboard wherever you want it to be on the map.

## How to make a dataset

Start Carla directly from Unreal Engine Editor by clicking the button `Play` in the latest software.
Then you will need to start OpenPilot.

```bash
cd openpilot/tools/sim
sudo ./start_openpilot_docker.sh --town=town01
```
`--town` being the town you opened with Unreal Engine.

Then into `CarlaScripts` folder we made a script to move the car in front of the billboard.
```bash
cd CarlaScripts/
python3.7 move_car_town01.py
```

Then we started simultaneously the car in OpenPilot and the script that captures the frame on OpenPilot.
```bash
python3.7 camera.py
```
The images are then saved into the folder `output`.

## How to test Dave v1 algorithm
Using the code from https://github.com/deepbillboard/DeepBillboard, we have been able to see the influence of the perturbation on the set of images we captured. All the tests we have done are in the `code` folder and are named like `test_output_...`.
In these tests, we tested the influence of different parameters such as the influence of the town, of the weather, of the size of the bollboard, as well as the angle of the camera.
In order to change the weather in a town, we used the script we have made called `change_weather.py` that is located in `CarlaScripts` folder.
To change the angle of the camera, we changed in `camera.py` the parameter called `rotation`.

To get the expected behaviour on the set of images, we used the `test.py` script.
```bash
cd code
python3.7 test.py -path='../CarlaScripts/output'
```
`-path` being the set of images we captured through OpenPilot.

The result is then created into the `test_output` folder.
