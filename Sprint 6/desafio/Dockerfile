FROM python:3

RUN apt-get update -y

WORKDIR /app

COPY . .

RUN pip install boto3

CMD ["python", "script.py"]