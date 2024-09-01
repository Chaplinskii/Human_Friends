FROM ubuntu:24.10
RUN apt-get update -y && apt-get install -y python3
#RUN git clone https://github.com/Chaplinskii/Human_Friends.git /app
WORKDIR /app
COPY /home/hacoc/my_app/ /app
CMD ["python3", "Human_Friends/main.py"]