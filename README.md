# test-automation-practice
Практика автоматизации тестирования с `pytest` и `selenium`

Объект тестирования: [http://automationpractice.com/](http://automationpractice.com/)

Окружение:
Тип|Описание
----|-----------
ОС|`Ubuntu Linux 18.04.4 LTS`
Python|`python 3.7`

### Как запустить тесты
Создайте виртуальное окружение и активируйте его.
```
$ mkvirtualenv testing --python=python3.7
```
Клонируйте репозиторий:
```
$ git clone https://github.com/ESm1th/test-automation-practice.git
```
Перейдите в директорию проекта:
```
$ cd test_automation_practice
```
Установите зависимости через `pip` используя зависимости из файла `requirements.txt`:
```
$ pip install -r requirements.txt
```
Данный проект работает с вебдрайверами `firefox` и `chrome`.

Нужно скачать драйверы соответствующих версий браузеров и добавить их в папку `$HOME/.local/bin/`

Для запуска тестов перейти в папку `tests`
```
$ cd tests
```
Тесты по умолчанию используют вебдрайвер `firefox`:
```
$ pytest -v
```

Для запуска тестов c вебдрайвером `chrome`:
```
$ pytest -v --browser=chrome
```

