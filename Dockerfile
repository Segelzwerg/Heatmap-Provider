FROM python:buster

MAINTAINER Marcel Haas "marcel.haas@hhu.de"

RUN apt update
RUN apt-get install git #python3 python3-dev py-pip build-base

COPY requirements.txt /app/requirements.txt

WORKDIR /app

#RUN python -m install --upgrade setuptools pip wheel
# somehow this does not update pip
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt

COPY app.py /app/app.py

ENTRYPOINT ["python"]
CMD ["app.py"]
EXPOSE 5000