FROM python:3-onbuild
COPY . /user/src/app
CMD ["python", "app.py"]


#docker build --tag python-flask-app:1.0 -f flask_Python.Dockerfile .
# 9099 is the port to access the service
# 9090 port is exposed by the application
#docker run -it  --rm --name flask-docker-demo-app -p 9099:9090 python-flask-app:1.0