# Docker Project : Front Angular / Back Django / Database Mongo 

JeanPaul / Martin / Thomas / Jesse

###### Requirements
docker
docker-compose


###### How to launch

```
git clone https://github.com/jgonneau/django_week.git
cd django_week
./dockrun.sh
```

```
sudo docker-compose up 
```
OR
```
sudo docker-compose up -d (-d for running processes in background)
```

##### Accès URL
```
localhost:8888 (front, Angular)
localhost:8000 (back, Python/Django)
```

##### Make migrations on Python
```
docker-compose exec djangoWeek_back bash

python manage.py makemigrations
python manage.py migrate
```


###### Note:
Please check the port are not already in use. It may have conflicts.
