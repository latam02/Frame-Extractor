FROM python:3.8-slim

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

WORKDIR /src

COPY requirements.txt /src/CONVERT_SERVICE/requirements.txt

RUN pip install --no-cache-dir -r /src/requeriments.txt 

COPY . .

EXPOSE 8085
