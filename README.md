## Building and Run locally via Docker

All of these commands assume you are in the root of the project.

Prerequisites

- Docker; if you don’t have it yet, follow the [installation instructions](https://docs.docker.com/install/#supported-platforms);
- Docker Compose; refer to the official documentation for the [installation guide](https://docs.docker.com/compose/install/).

To build and run in one command:

```shell
$ docker-compose -f local.yml up --build
```

This will spin up django and postgress containers and serve the application on port 8000.

### Building

```shell
$ docker-compose -f local.yml build
```

### Running

```shell
$ docker-compose -f local.yml up
```

## Development with Docker

#### Install requirements in your environment

```shell
$ pip install -r requirements/local.txt
```

#### Pre-commit and Type checks

Pre-commit

Install hooks to run code formatters(black,isort,flake8) on every commit

```shell
$ pre-commit install
```

Whenenver you commit, pre-commit will run checks against all python files in directory grid_points

Optionally run:

```shell
$ pre-commit run --all-files
```

#### Running django commands

These can be run by invoking the python shell then running the desired command e.g

```shell
# To create superuser
$ docker-compose -f local.yml run --rm django python manage.py createsuperuser

# To collectstatic
$ docker-compose -f local.yml run --rm django python manage.py collectstatic

# To start interactive shell
$ docker-compose -f local.yml run --rm django python manage.py shell

# or if you initialized already a container:
$ docker exec -it grid_points_django bash

# To check the logs out, run:
$ docker-compose -f local.yml logs
```

#### Database

To connect to the posgres database when the container is running:

```shell
$ docker exec -it grid_points_postgres psql -U root postgres
```

## Tests

The test suit can be run with

```shell
$ docker-compose -f local.yml run django pytest -v
```

## Django Admin and API Docs

To access django admin, got to `http://0.0.0.0:8000/admin/`
To access api swagger docs, go to `http://0.0.0.0:8000/docs/`

### Sample Request

URL: POST `http://localhost:8000/api/v1/points/`

Json Payload:
{
"points": "2,2;-1,30;20,11;4,5"
}
