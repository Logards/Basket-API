FROM python:3.12-slim

RUN apt-get update && apt-get install iputils-ping -y


WORKDIR /app


COPY . /app


RUN pip install --no-cache-dir -r requirements.txt


ENTRYPOINT ["uvicorn", "api:app", "--host", "0.0.0.0", "--reload"]