# flask_user_authentication

[Flask Authentication](https://www.freecodecamp.org/news/how-to-setup-user-authentication-in-flask/)

## Setting up

**Creating virtual environment**
`$ python -m venv env`

**Activate virtual environment**
`$ source env/bin/activate`

**Install dependencies**
`$ pip install -r requirements.txt`

**Add environment variables file**
`$ touch .env`
> Add any caracters you want for your secret key variable


**Initialize the database**
`$ flask db init`

**Migrate the database changes**
`$ flask db migrate`

**Apply migrations**
`$ flask db upgrade`

> remember that if it's your first time running the app, you'll need
> to run all the above commands.
> whenever you make changes to the database, you'll just need to run the last two commands.

**Running the server**
`$ python manage.py run`



