# VSCode Docker Django Debugging

## setup docker
```sh
docker run -v ${PWD}/app:/app -w /app python:3.9-alpine sh -c "pip install Django==3.2 && django-admin startproject app ."
docker-compose up --build
```
 
App runs on: http://127.0.0.1:8000/