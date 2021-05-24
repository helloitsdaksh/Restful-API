FROM ubuntu
RUN apt-get update
RUN apt-get install -y python python3-pip
RUN pip install flask flask_restful flask_cors
COPY Calculator_API.py /opt/Calculator_API.py
ENTRYPOINT FLASK_APP=/opt/Calculator_API.py flask run --host=0.0.0.0