FROM ubuntu:24.10
RUN apt-get update -y && apt-get install -y python3
WORKDIR /app
COPY ~/my_app/Human_Friends /app/
CMD ["python3", "~/app/Human_Friends/main.py"]