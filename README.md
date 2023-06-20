# weather_app

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

### Documentation: ###

* [Architecture overview](docs/architecture_overview.md)
* [Backend: Routine tasks](docs/commands.md)

### API documentation: ###

* ReDoc web UI: [http://127.0.0.1:8000/_platform/docs/v1/redoc/](http://127.0.0.1:8000/_platform/docs/v1/redoc/)

### First run: ###
Application is running in docker containers. 

### Prerequisites
Installed [docker](https://docs.docker.com/engine/install/)

Copy initial settings for Django project:

```bash
cp ./api/.env.example ./api/.env
```

Run application with required services:

```bash
make compose-up
```

Your application will be available at [http://localhost:8000](http://localhost:8000)

