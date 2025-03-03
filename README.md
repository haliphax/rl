# rl

Is roguelike, yes?

![Screenshot](https://github.com/haliphax/rl/blob/assets/screenshot.jpg?raw=true)

## Setup

### Develop

These steps are only necessary if you wish to contribute to the project.

<details>
<summary>Development setup</summary>

<br />

Use [`nvm`][] to select the appropriate node version:

```shell
nvm use  # you may need to `nvm install` first
```

Install node-based developer dependencies:

```shell
npm ci
```

Use [`pyenv`][] (or your virtual environment manager of choice) to create a
virtualenv with Python 3.12.1:

```shell
pyenv install 3.12.1
pyenv virtualenv 3.12 rl
pyenv activate rl
```

Install the project and its dependencies as editable:

```shell
pip install -e .[dev]
```

</details>

### Play

If you just want to run the game, you will first need Python 3.12.1. You can
either create a virtual environment or use docker.

Use [`pyenv`][] (or your virtual environment manager of choice) to create a
virtualenv with Python 3.12.1:

```shell
pyenv install 3.12.1
pyenv virtualenv 3.12 rl
pyenv activate rl
```

Install dependencies:

```shell
pip install .
```

<details>
<summary>Docker</summary>

<br />

To run the application in a docker container, build the image:

```shell
docker build -t rl:latest .
```

This image will need to be rebuilt any time `pyproject.toml` or requirements
are changed. Code/map changes will be reflected when running with live code (as
described below), otherwise the image will need to be rebuilt to incorporate
code/map changes, as well.

</details>

## Execute

Activate your virtual environment (ex. pyenv):

```shell
pyenv activate rl
```

Run the installed Python module:

```shell
python -m rl
```

<details>
<summary>Docker</summary>

<br />

Run a container using the previously-built image code/map files:

```shell
docker run --rm -it rl
```

Run a container with live code/map files (to test changes):

```shell
docker run --rm -it -v $(pwd)/rl:/app/rl rl
```

</details>

[`nvm`]: https://github.com/nvm-sh/nvm/blob/master/README.md#installing-and-updating
[`pyenv`]: https://github.com/pyenv/pyenv/blob/master/README.md#installation
