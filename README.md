# Teamwork
Software Engineering Senior Design CS116/117 (UCSC Winter/Spring 2017)

# Setting up a development environment to contribute

## Step 1: Python Virtual Enviornment
Note: Python 3.6 is assumed. Check your python version with `python --version`

If you don't have [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/) (it comes with python3 on some systems), install it with `pip install virtualenv`

Change to a directory where you want the teamwork-project directory to reside (e.g. `cd Documents/`)

Create a new venv (this will create a new folder with python installed and later django/dependencies)
```bash
$ virtualenv twdev
```
Note: you don't have to call your folder/venv "twdev"

Now cd into twdev (or whatever you named your venv) and activate it
```bash
$ source bin/activate
```
Note: you'll have to activate the venv anytime you want to work on this project. Consider adding an alias to your .bash_profile or .bashrc
```bash
alias tw="cd ~/Documents/twdev && source bin/activate"
```
You can always exit the venv with `deactivate`

## Step 2: Cloning the Repo
Optionally fork the teamwork-project repo. Clone it into the venv folder you just created. That's it, have a cookie.

## Step 3: Make a .env file based on .env.example
This is so we can keep the secret key hidden. It also allows us to use sqlite locally and postgres in production, neat.
For local develompent, your DATABASE_URL can be something like:
`DATABASE_URL=sqlite:////Users/sammyslug/Documents/twdev/teamwork-project/teamwork/db.sqlite3`

## Step 4: I forget
