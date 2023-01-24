# auto_smith
Web service automation training and demonstration project. Python, pytest, logging and Allure reports.



# Allure
https://docs.qameta.io/allure/#_get_started

## Установка Allure на ПК
Windows

Quickstart Scoop
```
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser # Optional: Needed to run a remote script the first time
> irm get.scoop.sh | iex
```
To install Allure, download and install Scoop and then execute in the Powershell:
```
scoop install allure
```


## Установка пакета allure для pytest
```
$ pip install allure-pytest 
```

Запуск из терминала Python
Запуск или всех или выбранного теста
```
python -m pytest --alluredir=test_results/

OR

python -m pytest --alluredir=test_results/ tests/ test_buy_product.py
```
Для открытия UI отчета Allure 
нужно перейти в корень папки и запустить след. команду
```
E:\Projects\auto_smith> allure serve test_results/
```

## For first build from docker compose file on Ubuntu
rusaykin@rusaykin-TM1703:~/projects/auto_smith$ sudo docker compose up -d


## DOCKER
Проверка образов в докере
sudo docker images -a

Прооверка запущенных контейнеров
sudo docker ps -a

Остановка контейнера в докере по id
sudo docker stop 216459e236c1

sudo docker run ad32e2967e5f

## Jenkins install 

sudo docker run -p 8080:8080 --name=jenkins-master jenkins/jenkins:latest

sudo docker start jenkins-master

sudo docker stop jenkins-master
home/jenkins_compose/jenkins_configuration


Logs of jenkins. You can find out admin pass here
sudo docker-compose logs -f jenkins

#Docker run with command
docker run --rm --mount type=bind,src=C:\Projects\auto_smith,target=/test_project/ pytest_runner

#Allure report
allure serve test_results/
