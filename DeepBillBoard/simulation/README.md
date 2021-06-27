# How to run the simulation in Carla

## Running the simulation

In order to do the simulation you will need to start carla, then open Town 1, put the billboard on the road next to the river. Finally launch the bash executable.

```
bash simulation.sh 
```

## Save the created images as a video

The images created during the simulation can be transforned into a video running the following command.

```
ffmpeg -i ./output/img_%03d.png simulation.mp4
```
