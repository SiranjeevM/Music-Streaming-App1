# FROM python:3.11.6

# ENV PYTHONBUFFERED 1

# WORKDIR /app

# ADD . /app

# COPY ./requirements.txt /app/requirements.txt

# RUN pip install -r requirements.txt

# COPY . /app

FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 8000


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]