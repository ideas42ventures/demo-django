# Django Demo App

An example web application written in Python, using Django.

## Contributing

- This is a dynamic app built using Python
- Hosted on Heroku in the ideas42 Ventures team account

### Requirements

- Python ^3.9
- [pyenv](https://github.com/pyenv/pyenv)
- [Poetry](https://python-poetry.org/docs/)

#### Recommended if using VSCode

- [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

### Local setup

Before starting this, ake sure you’ve installed the [requirements](#requirements).

**Clone the repo**

```
git clone git@github.com:ideas42ventures/demo-django.git
cd demo-django
```

**Install dependencies**

```
poetry install
```

**Enter Poetry Shell**

You will need to run all Django commands within the project’s virtual env.

```
poetry shell
```

**Note:** You can double check that you're using the virtual env by running `which python`. That should display a long path name to a python executable within a "virtualenvs" directory.

**Start the dev server**

```
python manage.py runserver
```

The app will be available at [http://localhost:8000](http://localhost:8000).
