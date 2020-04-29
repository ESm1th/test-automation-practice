Переключение контента и работа с ```iframe```
---------------------------------------------

Для примеров используется сайт [http://automationpractice.com/](http://automationpractice.com/)

Во всех примерах используется веб-драйвер `Firefox`

Будем считать что путь к драйверу прописан в переменной окружения `PATH`
```python
import pytest
from selenium.webdriver import Firefox
from selenium.webdriver.common.action_chains import ActionChains

URL = 'http://automationpractice.com/'

@pytest.fixture
def browser():
  driver = Firefox()
  driver.maximize_window()
  driver.implicitly_wait(3)
  yield driver
  driver.quit()

@pytest.fixture
def load(browser):
  browser.get(URL)

@pytest.fixture
def actions(browser):
  return ActionChains(browser)
```
Для переключения используется свойство драйвера `switch_to`, которое возвращает объект, на который переключается фокус, со всеми его опциями.
#### Переключение на активный элемент
```python
browser.switch_to.active_element
```
При таком переключении возвращается элемент на который установлен фокус либо элемент `<body>`, если ни один элемент не в фокусе.
```python
def test_active_element_body(browser, load):
  assert browser.find_element_by_tag_name('body') is browser.switch_to.active_element
```
Данный тест будет иметь статус `PASS`, т.к. страница только что загрузилась и в фокусе нет элементов.
```python
def test_active_element_not_body(browser, load, actions):
  search_input = browser.find_element_by_id('search_query_top')
  body = browser.find_element_by_tag_name('body')
  actions.move_to_element(search_input).click().perform()  # переключаем фокус
  assert body is browser.switch_to.active_element
```
Данный тест будет иметь статус `FAIL`, так как фокус сместился на елемент `<input id="search_query_top" ...>`.
