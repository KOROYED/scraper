FROM python:3.12-slim

RUN apt-get update && apt-get install -y tzdata && rm -rf /var/lib/apt/lists/*
ENV TZ=Europe/Kyiv

WORKDIR /usr/src/scraper

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .

CMD ["python", "-u", "./main.py"]