# Команда Galamtor

### Участники Хакатона “Лидеры цифровой трансформации” *2020*

## Инструкция по работе с проектом

*ПРИМЕЧАНИЕ:* полный функционал, включающий тестирование задач, данной версии проекта поддерживается только на **ОС Linux Ubuntu**

### 1. Установка необходимых библиотек

* Для **Linux Ubuntu**

  Установите фрэймворк *django*, на котором и сделан проект, введя в терминал комманды:
  `sudo apt update`
  `sudo apt install python3-django`

  (Язык *Python* уже предустановлен на системе Ubuntu)
  
  

* Для **Microsoft Windows**

  Первым шагом необходимо установить язык программирования Python (можно скачать с [официального сайта](https://www.python.org/))

  Далее, открыв командную строку, ввести следующую строку для установки Django:

  `python -m pip install Django`

### 2. Запуск проекта

После скачивания фреймворка необходимо [скачать архив с проектом](https://github.com/reyzor144/galamtor_mycode/tree/final_beta) и распаковать в удобную для вас папку. После этого на **Ubuntu** откройте данную папку в терминале, на **WIndows** - откройте папку в проводнике, после чего зажмите клавишу *shift* и нажмите правую кнопку мыши, в открывшемся окне запустите командную оболочку **Powershell**.

После этого в терминале **Ubuntu** введите команду: `python3 manage.py runserver`

Для **Windows** соответсвенно: `python manage.py runserver`

После этого у вас запустится локальный сервер, адрес которого будет выведен в терминале, и вы сможете открыть его в любом браузере.

### 3. Использование сайта

На главной странице зайта в верхнем правом углу есть кнопка *Login*, по нажатию на которую вам предложат авторизироваться или создать учетную запись. На сайте уже создана учетная запись администратора с *Username:* *admin* и *Password: admin*. Она может быть использована для управления сайтом по вкладке `адрес_вашего_сервера/admin`. 

После авторизации на главной странице станут доступны вкладки **Courses** и **личный кабинет**, который появится на месте кнопки *Login*. Если ваша учетная запись является учительской (что можно настроить через панель `/admin`, выбрав для соотвествующей записи свойство **Teacher**  вместо **Student**), то вы сможете создавать задачи с тестами через кнопку **Create**, вводя тесты в формате `входные_данные,входные_данные...входные_данные;входные_данные,...входные_данные;выходные_данные;...` и так далее. Слева у вас имеется меню выбора задачи с текстовым окном, куда можно ввести код и отправить.

На данный момент поддерживается использования языков **Python** и **C++**, язык *Python* выбран по умолчанию. К сожалению, пока смена языка может происходить лишь путем изменения переменной в исходном коде и *недоступна* для пользователя. 

