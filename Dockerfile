FROM python:alpine

WORKDIR /src

COPY . /src

RUN pip install --no-cache-dir -r requirements.yml

CMD ["python", "./jetson.py"]
