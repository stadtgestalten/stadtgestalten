# grouprise

grouprise is a platform destined to encourage and enable social action and solidarity in the context of your city. Bildet Banden!

## Quick Setup

### For administrators
You may want to install the latest [snapshot build](https://git.hack-hro.de/stadtgestalten/stadtgestalten/builds/artifacts/master/raw/build/debian/export/stadtgestalten.deb?job=deb-package) as a deb package. Please note that this is a rather dirty package (embedded dependencies; suitable for Debian Stretch).

### For developers
1. You will need [virtualenv](https://virtualenv.pypa.io/en/stable/), [node](https://nodejs.org/en/) (downloaded automatically if unavailable), [python3](https://www.python.org/), [flake8](http://flake8.pycqa.org/en/latest/), [pip](https://pip.pypa.io/en/stable/) and [make](https://www.gnu.org/software/make/) to get started. If you have all of those, you may proceed :). Otherwise see the Dependencies Section
2. Run `make app_run` and wait until you see something like `Starting development server at http://127.0.0.1:8000/`
3. Visit http://127.0.0.1:8000/

## Dependencies

Depending on your distribution (we assume you’ll be using something like Linux here) the build dependencies of this project will be available via your package manager.

Some additional dependencies will be downloaded during the build process:

* pip (Python): `requirements.txt`
* npm (NodeJS): `package.json`

### Debian
For `virtualenv`, `python3`, `flake8` and `pip` use apt:
```sh
apt install make virtualenv python3 python3-flake8 python3-pip python3-sphinx python3-recommonmark python3-xapian
```

Additionally `node` v8.12 or later and `npm` are required.  Both are available in Stretch-Backports and Buster.  If you do not have a suitable version installed, it will be automatically downloaded when running `make` (see `make.d/nodejs.mk`).

### Arch Linux
Fortunately all of the required packages are available via pacman.
```sh
pacman -Sy make nodejs npm flake8 python python-virtualenv python-pip python-sphinx python-recommonmark python-xapian
```


## Local Settings

Your local Django settings will be located in `stadt/settings/local.py`. Use `make app_local_settings` to create a default configuration. 


## Database Setup

The preconfigured database is a local sqlite file.
For production deployment you should use a database server.

### PostgreSQL

The following statement creates a suitable database including proper collation settings:

    CREATE USER grouprise WITH PASSWORD 'put random noise';
    CREATE DATABASE grouprise WITH ENCODING 'UTF8' LC_COLLATE='de_DE.UTF8' LC_CTYPE='de_DE.UTF8' TEMPLATE=template0 OWNER grouprise;

The command above requires the locale 'de_DE.UTF8' in the system of the database server.


## Docker deployment

[Docker](https://docker.io/) may be used for a quick and dirty way to set up an instance of
grouprise.

The docker image based on the latest released deb package of grouprise can be built easily:
```sh
docker build docker/grouprise-released-deb
```


## Production deployment

We recommend to use the provided deb package. It contains an nginx and UWSGI configuration.

See also [deb.md](./docs/deployment/deb.md).


## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md)
