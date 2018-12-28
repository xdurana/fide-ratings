# flask-docker-ci

[![Build Status](https://travis-ci.org/xdurana/flask-docker-ci.svg?branch=master)](https://travis-ci.org/xdurana/flask-docker-ci)

A `Flask` boilerplate REST API built with `flask-restplus`, running in `Docker` and on continuous integration with `TravisCI` and `pytest`.

## Running

```sh
docker-compose up
docker exec -it mycontainer /bin/ash
flask run --host=0.0.0.0 --port=80
```
