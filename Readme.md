# JWT user login system with python and sqlite

This repo is meant to be a play ground on creating a custom login and jwt authentication microservice with python. 

## Run instructions

`export FLASKAPP=app.py`

`python3 -m flask run`


## Usage


**Create User**

```bash
curl --header "Content-Type: application/json" --request POST --data '{"username":"<username>","password":"<password>","email":"<emailaddress>"}' http://localhost:5000/register

```

**Login, get a token**

```bash
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"username":"<username>","password":"<password>"}' \
  http://localhost:5000/login
```

## Development

Configured for VSCode remote development.

`docker-compose up -d`

Open base directory in vscode with remote container plugin installed.
Click reopen in container.

click into importer.py, hit the debug button. A test server will start and listen on 
port 5000. 