FROM python:3.12-slim
RUN apt-get update -y && apt-get install -y vim nano
WORKDIR /home/python/app
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /home/python/app
CMD ["python", "main.py" ]