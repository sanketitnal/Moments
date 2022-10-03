# Moments
Django + S3 bucket image gallery for personal use

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/sanketitnal/Moments.git
$ cd Moments
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:

Create S3 bucket and add relevant details in gallery/secrets.py file
```
#Add following details

AWS_S3_ACCESS_KEY_ID = 'YOUR-S3-ACCESS-KEY'
AWS_S3_SECRET_ACCESS_KEY = 'YOUR-S3-SECRET-KEY'
AWS_STORAGE_BUCKET_NAME = 'YOUR-S3-STORAGE-BUCKET-NAME'

```

Run following commands for 1 time setup
```sh
(env)$ python manage.py makemigrations
(env)$ python manage.py migrate
(env)$ python manage.py createsuperuser
```

To run server
```sh
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.


![App preview picture](https://github.com/sanketitnal/Moments/blob/master/moments.png?raw=true)
References: https://www.youtube.com/c/DennisIvy
