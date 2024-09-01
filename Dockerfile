FROM ubuntu:24.10
RUN apt-get update -y && apt-get install -y git python3
RUN git clone https://github.com/Chaplinskii/Human_Friends.git /app
WORKDIR /app
#COPY ~/my_app/Human_Friends /app
CMD ["python3", "./Human_Friends/main.py"]