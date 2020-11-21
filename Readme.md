# JWT user login system with python and sqlite

This repo is meant to be a play ground on creating a custom login and jwt authentication microservice with python. 

## Run instructions

`export FLASKAPP=app.py`

`python3 -m flask run`


## Usage

**Create User**

```bash
curl --header "Content-Type: application/json" --request POST --data '{"username":"<username>","password":"<password>","email":"<emailaddress>"}' http://<flaskid>:<port>/register

```

**Login, get a token**

```bash
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"username":"<username>","password":"<password>"}' \
  http://<flaskid>:<port>/login
```
