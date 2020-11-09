FROM arm64v8/python:buster
WORKDIR /code
ENV FLASK_APP App/app.py
ENV FLASK_RUN_HOST 0.0.0.0
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD ["flask", "run"]