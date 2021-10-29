FROM python:3.8-slim

# This prevents Python from writing out pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# This keeps Python from buffering stdin/stdout
ENV PYTHONUNBUFFERED 1

WORKDIR /src

COPY requirements.txt /src/requirements.txt

RUN pip install -r CONVERT_SERVICE/requirements.txt --no-cache-dir

# Install application into container
COPY . .

EXPOSE 8085

ENTRYPOINT ["python","./CONVERT_SERVICE/convert_service/manage.py","runserver"]
