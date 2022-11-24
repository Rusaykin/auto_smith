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
