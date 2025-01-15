# git-lession

# Setting up My WEB site 2.0.1

## Set up your python virtual environment (virtualenv)

You will probably have the virtualenv builder already installed on your machine; if not,
go to the [virtualenv documentation](https://pypi.python.org/pypi/virtualenv).

Once you have the virtualenv builder installed, you will want to create your virtualenv
and install the necessary packages using pip.

To create the virtualenv:

    virtualenv env

This creates a directory called "env" in your current working directory. Inside this 
directory there is an activate shell script that activates your virtualenv.

    . env/bin/activate

Your prompt should change to show you are currently using the virtualenv. To exit the
virtualenv, use the function deactivate.

Now we use pip to install the necessary packages into the new virtualenv. I have created a
requirements file with the correct versions for the packages we are using.

    $ pip install -r requirements/development.txt

# Running the development server

The django-extensions package includes a really nice development server that can be
invoked using the runserver_plus subcommand.

    cd development
    python manage.py runserver_plus 0.0.0.0:8025

If you visit the URL in your browser you should see the front page of the site.
