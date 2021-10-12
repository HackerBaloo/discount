#!/bin/bash
python3 -m venv venv
echo "run: . ./venv/bin/activate"
pip install nameko-redis
docker run -d -p 5672:5672 --hostname nameko-rabbitmq rabbitmq:3
docker run --name my-redis-container -d redis
nameko run messagequeue