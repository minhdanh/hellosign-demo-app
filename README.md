hellosign-demo-app
==================

A demo app wrriten in Python for hellosign_python_sdk

### How to use

#### 1. Clone the source and install django

````bash
git clone git@github.com:minhdanh/hellosign-demo-app.git
cd hellosign-demo-app
pip install django=1.6
````

#### 2. Edit settings

Copy `settings.py.sample` to `settings.py` in `hellosign/`. Then update the file with your own `API_KEY` and `CLIENT_ID` and `SECRET`.
If you're deploying the app on Heroku, you may want to keep the sample content and use Heroku environment variables instead.
Notice that in order for the app to run correctly, you need to register your HelloSign app with a valid callback url. Unfortunately, HelloSign doesn't allow us to use localhost or 127.0.0.1 as the callback url, so if you're trying to run the app on your local machine, you may consider editing your hosts file (/etc/hosts) to resolve the domain of the callback url to `127.0.0.1`.

#### 3. Start the server

````
python manage.py runserver
````

Or just push the code to Heroku and you're all set!
