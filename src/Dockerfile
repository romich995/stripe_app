FROM python:3.10-alpine
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /src

COPY ./requirements.txt ./requirements.txt

RUN pip install -r ./requirements.txt

COPY . .
EXPOSE 8000