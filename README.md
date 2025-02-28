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

Use [`pyenv`][] or your virtual environment manager of choice to create a
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
either use your system Python, create a virtual environment, or use docker.

<details>
<summary>Virtual environment setup</summary>

<br />

If you don't want to use your system Python installation, use [`pyenv`][] or
your virtual environment manager of choice to create a virtualenv with Python
3.12.1:

```shell
pyenv install 3.12.1
pyenv virtualenv 3.12 rl
pyenv activate rl
```

</details>

For both system Python and virtual environments, you must install dependencies:

```shell
pip install .
```

<details>
<summary>Docker</summary>

<br />

To run the application in a docker container, first build the image:

```shell
docker build -t rl:latest .
```

Then run a container using the image rather than using the standard
execution instructions:

```shell
docker run --rm -it rl
```

</details>

## Execute

Run the installed Python module:

```shell
python -m rl
```

[`nvm`]: https://github.com/nvm-sh/nvm/blob/master/README.md#installing-and-updating
[`pyenv`]: https://github.com/pyenv/pyenv/blob/master/README.md#installation
