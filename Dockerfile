FROM ubuntu:23.10

RUN apt update
RUN apt -y upgrade

RUN apt install -y python3.11
RUN apt install -y python3-pip
RUN pip install pip==22.3.1 --break-system-packages

RUN apt install -y curl
RUN apt install -y git
RUN mkdir /root/.u2net
RUN curl -o /root/.u2net/u2net.onnx https://github.com/danielgatis/rembg/releases/download/v0.0.0/u2net.onnx

WORKDIR /root/app
COPY . .

RUN pip3 install -r requirements.txt

CMD ["python3", "main.py"]
