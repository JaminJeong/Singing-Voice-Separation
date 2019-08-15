#!/bin/bash
/usr/bin/xhost +

HOME=$HOME
default=1.0
tag=${1:-$default}
echo $tag
NAME=tf${USER}$(date +%Y%m%d%H%M%S)

sudo nvidia-docker run -it \
  --name ${NAME}_${tag} \
	--privileged \
  -v /etc/group:/etc/group:ro \
  -v /etc/passwd:/etc/passwd:ro \
	-v /tmp/.X11-unix:/tmp/.X11-unix \
  -v /dev/video0:/dev/video0 \
  -v $HOME:$HOME \
  -w=$(pwd) \
	-e DISPLAY=$DISPLAY \
	-e TZ=Asia/Seoul \
  -e QT_X11_NO_MITSHM=1 \
  -p 6006:6006 \
  tfscunet:$tag \
  /bin/bash

