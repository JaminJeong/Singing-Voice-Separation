ARG VERSION

FROM tensorflow/tensorflow:$VERSION

RUN apt update && apt install -y vim git wget libsndfile1
RUN apt install -y libav-tools 

RUN pip3 install -U pip

RUN pip3 install librosa==0.6.2
RUN pip3 install numpy==1.14.3
RUN pip3 install pydub

RUN pip3 install wget
