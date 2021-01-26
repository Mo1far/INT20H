# CheapestBuckwheat [INT20H test-task]

##### This project can compare prices of buckwheat in 3 stores: rozetka.com.ua, Auchan and Novus.

#### How to run it?
```
git clone
virtualenv -p=python3.8.5 .env
source .env/bin/activate
pip install -r requirements.txt
docker-compose up --build
docker-compose exec web python manage.py migrate --noinput
docker-compose run web INT20H.wsgi:application --bind 127.0.0.1:8000
```

#### Main technologies
```
Django - backend of our project
Bootstrap - UI kit for beautiful site
BeautifulSoup - instrument which parse buckwheat on 3 markets
Docker - to make your deploy easily
```

### Check the site > http://hacktest.elit-bugtracker.tk/
