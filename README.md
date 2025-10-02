# Обрезка ссылок с помощью VK
## Цель проекта

Этот проект — консольная утилита, которая сокращает длинные ссылки через сервис vk.cc, проверяет, является ли ссылка уже сокращённой, и считает общее количество переходов по сокращённой ссылке. Скрипт написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).

## Требования к окружению

Проект работает на операционных системах Windows, Linux и macOS. Требуется Python версии 3.8 и выше. Для работы скрипта необходимы библиотеки requests и python-dotenv. 

## Как установить

Сначала нужно клонировать репозиторий и перейти в папку проекта:

```python
git clone https://github.com/Adelina2302/VK_Lesson_-1_Dunina
cd repo
```

Далее установить зависимости:


```python
pip install -r requirements.txt
```

В корне проекта создаётся файл .env, в который записывается токен VK API в формате:

```python
VK_TOKEN=ваш_токен
```

Токен можно получить, создав Standalone-приложение в VK и запросив `access_token`.

## Примеры запуска

Сокращение длинной ссылки:

```python
python main.py https://example.com
```

Вывод в консоль:

![Output](https://github.com/Adelina2302/VK_Lesson_-1_Dunina/blob/main/images/VK_pic1.png)


Получение статистики по короткой ссылке:

```python
python main.py https://vk.cc/abc123
```

Вывод в консоль:

![Output](https://github.com/Adelina2302/VK_Lesson_-1_Dunina/blob/main/images/VK_pic2.png)

Ошибка при некорректной ссылке:

```python
python main.py example.com
```

Вывод в консоль:

![Output](https://github.com/Adelina2302/VK_Lesson_-1_Dunina/blob/main/images/VK_pic3.png)

## API проекта

В проекте доступны функции, которые можно использовать через импорт. Функция `is_shorten_link(token, url)` возвращает True, если ссылка уже сокращённая, и False в противном случае. Функция `shorten_link(token, url)` возвращает сокращённую ссылку через VK API. Функция `count_clicks(token, link)` возвращает общее количество переходов по сокращённой ссылке.
