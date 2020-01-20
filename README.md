# PINTS benchmark REST API

## Overview

A REST API for evaluating likelihoods arising from from real problems in 
electrochemistry, cardiac electrophysiology, (others?), for testing new inference 
techniques

This project uses the [Connexion](https://github.com/zalando/connexion) library on top 
of Flask.

## Requirements
Python 3.5.2+

## Usage
To run the server locally, please execute the following from the root directory:

```
pip3 install -r requirements.txt
python3 -m swagger_server
```

and open your browser to here:

```
http://localhost:5000/pints-team/benchmarks/1.0.0/ui/
```

To launch the unit tests, use nosetests

```
nosetests
```

To launch the integration tests, use tox:
```
sudo pip install tox
tox
```

## Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
# building the image
docker build -t swagger_server .

# starting up a container
docker run -p 8080:8080 swagger_server
```

## Deploying

There is a test heroku server here

```
https://mighty-badlands-12664.herokuapp.com/pints-team/benchmarks/1.0.0/ui/
```

To deploy changes to this server add the `heroku` remote and push the changes

```
git remote add heroku https://git.heroku.com/mighty-badlands-12664.git
git push heroku master
```
