FROM ubuntu:24.10
RUN apt-get update -y && apt-get install -y git python3 pip
RUN git clone https://github.com/Chaplinskii/Human_Friends.git /app
WORKDIR /app
RUN pip install pymysql
#COPY /home/hacoc/my_app/ /app
#CMD ["ls"]
CMD ["python3", "main.py"]
