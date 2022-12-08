Подготовка системы
В качестве предварительной настройки обновим список пакетов, зададим корректное время сервера и настроим брандмауэр.

Обновление списка пакетов в репозиториях
Для возможности установки свежих пакетов, выполняем команду:

apt update

Настройка времени
Для настройки времени зададим часовой пояс:

timedatectl set-timezone Europe/Moscow

* в данном примере московское время.

Установим службу для синхронизации времени:

apt install chrony

Разрешим ее автозапуск: 

systemctl enable chrony

Настройка брандмауэра
По умолчанию в Ubuntu настроены разрешающие правила и конфигурирование брандмауэра не требуется. Однако, если в нашей системе применяются правила, необходимо открыть порт 8080, на котором работает Jenkins:

iptables -I INPUT -p tcp --dport 8080 -j ACCEPT

И сохраняем правило:

apt install iptables-persistent

netfilter-persistent save

Инсталляция Jenkins
Как было сказано выше, мы установим openjava, сервис Jenkins и завершим развертывания на портале. Итого, 3 этапа.

1. Установка openjdk
Выполняем команду:

apt install default-jdk

Выбираем реализацию java по умолчанию с помощью утилиты update-alternatives:

update-alternatives --config java

Скорее всего, мы увидим сообщение:

There is only one alternative in link group java (providing /usr/bin/java): /usr/lib/jvm/java-11-openjdk-amd64/bin/java
Nothing to configure.

Это значит, что в системе установлена только одна реализация java. Но если их несколько, на запрос:

  Selection    Command
-----------------------------------------------
*+ 1           java-11-openjdk.x86_64 (/usr/lib/jvm/java-11-openjdk-11.0.9.11-0.el8_2.x86_64/bin/java)

... выбираем вариант с подходящей версией, например, последней:

Enter to keep the current selection[+], or type selection number: 1

Готово. Смотрим версию установленной java:

java -version

Мы должны увидеть что-то на подобие:

openjdk version "11.0.17" 2022-10-18
OpenJDK Runtime Environment (build 11.0.17+8-post-Ubuntu-1ubuntu220.04)
OpenJDK 64-Bit Server VM (build 11.0.17+8-post-Ubuntu-1ubuntu220.04, mixed mode, sharing)

2. Установка Jenkins
Для установки сервиса Jenkins добавляем репозиторий:

vi /etc/apt/sources.list.d/jenkins.list

deb https://pkg.jenkins.io/debian-stable binary/

Импортируем публичный ключ для подключения к репозиторию:

wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -

Обновляем список пакетов:

apt update

Устанавливаем jenkins:

apt install jenkins

Разрешаем автозапуск сервиса:

systemctl enable jenkins

3. Завершение установки
Открываем браузер и переходим по адресу http://<IP-адреса сервера Jenkins>:8080 — откроется окно «Unlock Jenkins». В нем будет путь до файла, в котором нужно взять парольную фразу для разблокировки портала:

Стартовая страница установки Jenkins

И так, на сервере вводим команду:

cat /var/lib/jenkins/secrets/initialAdminPassword

* где /var/lib/jenkins/secrets/initialAdminPassword — полный путь до файла, который отображен на стартовой странице установки.

Мы должны увидеть что-то на подобие:

# cat /var/lib/jenkins/secrets/initialAdminPassword
35635dce8b014707a2ec90937763cfe3

Используем данный пароль и вставляем его в поле Administrator password:

Вводим парольную фразу для установки портала

В следующем окне выбираем вариант установки плагинов — рекомендованные или по выбору:

Устанавливаем плагины для портала

* если мы не слишком хорошо знакомы с продуктом, выбираем рекомендованные плагины.

Начнется процесс развертывания Jenkins:

Начинается установка портала

После создаем учетную запись для администратора:

Создаем пользователя после установки

На последней странице мы можем задать URL-адрес для нашего портала (или оставить IP-адрес):

Задаем адрес URL для Jenkins

Установка завершена.

Другие способы установки
Кратко, рассмотрим другие методы установки Jenkins.

1. Docker
Если Docker не установлен в системе, выполняем инсталляцию.

После загружаем контейнеры для Jenkins: 

docker pull jenkins/jenkins

Запускаем контейнер:

docker run -p 8080:8080 --name=jenkins-master jenkins/jenkins:latest

На экране мы должны увидеть код для разблокировки Jenkins. Копируем его, открываем в браузере страницу http://<IP-адреса сервера Jenkins>:8080 и выполняем установку в веб, как это делали выше.

После выполнения установки прерываем работу контейнера в интерактивном режиме комбинацией Ctrl + С и запускаем его в бэкграунде:

docker start jenkins-master

2. Установка из файла WAR
Загружаем последнюю версию war-файла:

wget -P /usr/local/bin/ http://mirrors.jenkins-ci.org/war/latest/jenkins.war

* на странице загрузки jenkins можно найти ссылку для скачивания LTS-версии файла war. Обратите внимание, что мы сразу размещаем файл в каталоге /usr/local/bin.

Запускаем war с помощью java:

java -jar /usr/local/bin/jenkins.war

На экране мы должны увидеть код для разблокировки Jenkins. Копируем его, открываем в браузере страницу http://<IP-адреса сервера Jenkins>:8080 и выполняем установку в веб, как это делали выше.

После выполнения установки прерываем работу war в интерактивном режиме комбинацией Ctrl + С.

Создаем юнит в systemd:

vi /usr/lib/systemd/system/jenkins.service

[Unit]
Description=Jenkins Service
After=network.target

[Service]
Type=simple
User=root
ExecStart=/usr/bin/java -jar /usr/local/bin/jenkins.war
Restart=on-abort
ExecReload=/bin/kill -HUP $MAINPID

[Install]
WantedBy=multi-user.target

Перечитываем юниты в systemcd:

systemctl daemon-reload

Разрешаем автозапуск сервиса jenkins и стартуем его:

systemctl enable jenkins --now

Можно проверить состояние запущенной службы командой:

systemctl status jenkins

Работа с Jenkins в CLI
По умолчанию, необходимый для работы с Jenkins из командной строки файл jenkins-cli.jar не копируется в систему.

Его нужно скачать. Выполняем:

wget http://127.0.0.1:8080/jnlpJars/jenkins-cli.jar -P /usr/local/bin/

* таким образом, мы скачаем файл с собственного сервера и разместим его в папке /usr/local/bin/.

Теперь можно выполнять команды с синтаксисом:

java -jar /usr/local/bin/jenkins-cli.jar -auth <имя пользователя>:<пароль> -s http://127.0.0.1:8080/ <выполняемые команды и опции>

Например, получить список команд можно так:

java -jar /usr/local/bin/jenkins-cli.jar -auth admin:admin -s http://127.0.0.1:8080/ -webSocket help

* где admin:admin — логин и пароль от административной учетной записи.

Установка плагинов
Список плагинов мы можем найти на официальном сайте. Мы рассмотрим 2 способа их установки — из веб-интерфейса и командной строки.

Веб-интерфейс
Переходим в раздел Настроить Jenkins:

Переход к настройкам Jenkins

Затем в Управление плагинами:

Переход к управлению плагинами в Дженкинс

Переходим к вкладке Доступные, по фильтру находим нужный нам плагин, отмечаем галочкой его установку:

Находим и выбираем для установки нужный нам плагин

Кликаем по кнопке Загрузить и установить после перезагрузки:

Устанавливаем плагин

Будет выполнена установке плагина, после чего, портал перезапустит сервис.

CLI
В командной строке для установки плагина выполняем:

java -jar /usr/local/bin/jenkins-cli.jar -auth admin:admin -s http://127.0.0.1:8080/ install-plugin docker-workflow

* в данном примере мы установим плагин Docker Pipeline. Обратите внимание, что его идентификатор для установки docker-workflow — посмотреть данный идентификатор можно на сайте с плагинами.

После перезапускаем сервис jenkins:

systemctl restart jenkins

Плагин установлен.

Возможные ошибки
Error: Unable to access jarfile jenkins-cli.jar
Ошибка появляется при попытке выполнить команду в jenkins-cli.

Причина: для работы команды необходим файл jenkins-cli.jar, который не устанавливается в системе.

Решение: выполняем действия по настройке системы для работы с jenkins-cli.

failed to start lsb: start jenkins at boot time
Ошибка возникаем при попытке запустить сервис jenkins.

Причина: как правило, отсутствие в системе установленного java.

Решение: устанавливаем java по инструкции выше.