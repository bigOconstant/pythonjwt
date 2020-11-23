# JWT user login system with python and sqlite

This repo is meant to be a play ground on creating a custom login and jwt authentication microservice with python and sqlite with postgres support likely comming in the future. 

## Run instructions

Expects a user.db file mounted in app directory. See docker-compose run for example

## Secrets.

Needs an environment variable **SECRET** to encode and decode tokens


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

Configured for VSCode remote container development.

`docker-compose build`

Builds a container with your current user as the user

`docker-compose up -d`

Open base directory in vscode with remote container plugin installed. You can do this in bash with,

`code .`


Click reopen in container. or `f1->remote in container`

Click debug play button and run


## Testing

A REST Client plugin is installed by default in the vscode remote development enviornment.

Once connected in VSCode you can click in the file testendpoints.http and click send request



