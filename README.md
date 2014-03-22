hellosign-demo-app
==================

A demo app wrriten in Python for hellosign_python_sdk

### How to use

#### 1. Install django

````bash
pip install django=1.6
````

#### 2. Edit settings

Copy `settings.py.sample` to `settings.py` in `hellosign/`. Then update the file with your own `API_KEY` and `CLIENT_ID` and `SECRET`.
If you're deploying the app on Heroku, you may want to keep the sample content and use Heroku environment variables instead.

#### 3. Start the server

````
python manage.py runserver
````

Or just push the code to Heroku and you're all set!
