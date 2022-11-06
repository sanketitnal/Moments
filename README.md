# Moments
Django + S3 bucket image gallery for personal use

## Setup
Clone the repository:

```sh
$ git clone https://github.com/sanketitnal/Moments.git
$ cd Moments
```
* [Setup AWS S3 and access key](#s3-setup)
* [Add S3 credentials](#s3-credentials)
* Either one of the following
  - [Run using docker](#docker-setup)
  - [Run on local machine](#local-setup)

<a name="s3-setup"></a>
## S3 setup
1. Create a S3 bucket.
2. Refer <a href="https://bobbyhadz.com/blog/aws-s3-allow-public-read-access"> make-s3-objects-public </a> to make the bucket public.
3. Create AWS IAM user with credential type = Access key - Programmatic access. Use the generated credential details.

<a name="s3-credentials"></a>
## Add S3 credentials
Add AWS access key details generated in previous section to gallery/secrets.py file.(You might need to create this file)
```
#Add following details
AWS_S3_ACCESS_KEY_ID = 'YOUR-S3-ACCESS-KEY'
AWS_S3_SECRET_ACCESS_KEY = 'YOUR-S3-SECRET-KEY'
AWS_STORAGE_BUCKET_NAME = 'YOUR-S3-STORAGE-BUCKET-NAME'
```

<a name="docker-setup"></a>
## Run on Docker
* Install docker if you haven't <a href="https://docs.docker.com/engine/install/">docker-install</a>.
* From project's directory, run following command.
```
docker build . -t moments-app
```
  - Above command creates a docker image.
  - -t is used to add tag to the image.
* If everything runs properly, a docker image will be generated. You can confirm it using -
```
docker image ls
```
* Create and run the application container using
```
docker container run --name moments --publish 8000:8000 moments-app
```
* Open `http://127.0.0.1:8000/` 

<a name="local-setup"></a>
## Run on Local Machine
* Create a virtual environment to install dependencies in and activate it:
```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

* Install the dependencies:
```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:

* Create S3 bucket and 

* Run following commands for 1 time setup
```sh
(env)$ python manage.py makemigrations
(env)$ python manage.py migrate
(env)$ python manage.py createsuperuser
```

* To run server
```sh
(env)$ python manage.py runserver
```
Open `http://127.0.0.1:8000/`.


## References
![App preview picture](https://github.com/sanketitnal/Moments/blob/master/moments.png?raw=true)
References: https://www.youtube.com/c/DennisIvy
