FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app/backend
COPY requirements.txt /app/backend

RUN pip3 install --upgrade pip -r requirements.txt

COPY . /app/backend

EXPOSE 8000
