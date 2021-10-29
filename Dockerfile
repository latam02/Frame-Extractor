FROM python:3.8-slim

# This prevents Python from writing out pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# This keeps Python from buffering stdin/stdout
ENV PYTHONUNBUFFERED 1

WORKDIR /src

COPY ./CONVERT_SERVICE/requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir 

# Install application into container
COPY . .

EXPOSE 8085

ENTRYPOINT ["python","manage.py","runserver"]
