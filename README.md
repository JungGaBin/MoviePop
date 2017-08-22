# MoviePop

Predict Number of Movie Viewers

## Model Info
```
movie_data.xlsx - All Data
dataset.csv - Training DataSet
movie_parse.py - Parse Naver Movie Data
movie_train.py - Train Model
movie_serve.py - Serve Model
```

## Requirement
* Python 3.6.0
* Tensorflow 1.2.1
* Django 1.11.3
* BeautifulSoup 4.4.0


## Usage
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```