# Django Demo App

An example web application written in Python, using Django.

## Contributing

- This is a dynamic app built using Python
- Hosted on Heroku in the ideas42 Ventures team account

### Requirements

- Python 3.9.1
- [pyenv](https://github.com/pyenv/pyenv)
- [Poetry](https://python-poetry.org/docs/)

#### Recommended if using VSCode

- [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

### Local setup

Before starting this, make sure you’ve installed the [requirements](#requirements).

**Clone the repo**

```
git clone git@github.com:ideas42ventures/demo-django.git
cd demo-django
```

**Install and set the supported python version**

⚠️ **This is a first time install snag point**

Before attempting to install dependencies your local pyenv version must be set to the supported version in `.python-version`.

If you have that version installed already, pyenv will switch to it automatically. Check to see what version you're on with:

```
pyenv version
```

If you see a message that the version is not installed, you need to install it:

```
pyenv install
```

pyenv will switch to the version automatically. You can check to make sure with `pyenv version`.

**Install dependencies**

```
poetry install
```

**VSCode note** If you are prompted to use a python environment for your workspace, say yes.

**Enter Poetry Shell**

You will need to run all Django commands within the project’s virtual env.

```
poetry shell
```

**Note:** You can double check that you're using the virtual env by running `which python`. That should display a path to a python executable in a local `.venv` directory.

**Start the dev server**

```
python manage.py runserver
```

The app will be available at [http://localhost:8000](http://localhost:8000).

## Deployment

This app is hosted on Heroku.
