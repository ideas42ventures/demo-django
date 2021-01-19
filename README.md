# Django Demo App

An example web application written in Python, using Django.

## Contributing

- This is a dynamic app built using Python 3.8+
- Hosted on Heroku in the ideas42 Ventures team account

### Requirements

- Python 3.8+
- [Poetry](https://python-poetry.org/docs/)

#### For VSCode

- [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
-

### Local setup

Make sure you’ve installed the [Requirements](#requirements).

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

### VSCode Notes

If you are using VSCode there are extra setup steps needed.

**If you get a warning that "Formatter black is not installed. Install?"**

Don't choose any of the options. You need to tell VSCode where this project's virtual env is located. **Note** this is a [community-wide issue](https://github.com/microsoft/vscode-python/issues/8372) that will improve over time.

Those won't work with the Poetry virtual env. Instead, you will need to create local configuration.
