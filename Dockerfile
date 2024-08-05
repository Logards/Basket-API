FROM rockylinux:9
RUN dnf update -y
RUN dnf install python3.12 -y
RUN dnf install python3.12-pip -y
WORKDIR /Basket-API
ADD . /Basket-API
RUN pip3.11 install -r requirements.txt
ENTRYPOINT ["uvicorn", "api:app", "--host", "0.0.0.0", "--reload"]