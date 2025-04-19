VD08. Работа с API
✅ API (Application Programming Interface) — это набор правил и методов, позволяющих различным программам взаимодействовать друг с другом. API предоставляет способ для программного обеспечения запрашивать и обмениваться данными с другими программами или сервисами.

На самом деле мы зачастую используем сервисы, в которых задействованы API, даже не подозревая об этом. Например данные о курсах валют берутся из основного источника и передаются через API в приложение, которым мы пользуемся.

API можно сравнить с договором между клиентом и продавцом. Клиентом при этом выступает приложение, которому нужны данные, а продавцом — сервер, на котором эти данные хранятся.

Сферы применения API

Языки программирования:
Помогает функциям корректно взаимодействовать друг с другом.
Обеспечивает передачу информации между функциями.
Операционные системы:
Позволяет получать данные из памяти.
Обеспечивает передачу данных.
Взаимодействие сервисов:
Сервисы могут общаться друг с другом.
Можно строить программы, используя API.
Некоторые документации могут быть оформлены лучше, другие хуже, но все они пригодны для использования.



Теперь рассмотрим, почему API так популярны среди программистов. В первую очередь потому, что они предоставляют доступ к готовым инструментам. Существуют готовые наборы функций, которые можно использовать для быстрого создания приложений или программ. Например, если нужно создать приложение для отображения курсов валют, API позволяет сделать это быстрее и дешевле, чем разрабатывать всё с нуля. Даже если API платное, его использование обычно обходится дешевле, чем разработка аналогичной функциональности с нуля.

Существуют множество популярных API, например:

Google Maps API — позволяет добавлять карты на сайт;
Weather API — предоставляет информацию о погоде;
Payment Gateway API — позволяет обрабатывать платежи на вашем сайте, что полезно для интернет-магазинов (PayPal, Stripe).
____
API (Application Programming Interface) могут быть разных типов, и для их использования часто требуется регистрация на сайте, который предоставляет API. После регистрации мы получаем ключ доступа или токен, который необходим для отправки запросов к API.

Разработчики API используют авторизацию через токен по нескольким причинам:

Ограничение частоты запросов: это помогает предотвратить перегрузку серверов.
Платные подписки: возможность снять ограничения на количество запросов за плату.
Большинство API, даже если они бесплатные, требуют регистрации и получения токена. Мы будем использовать API, у которого есть платная и бесплатная версия, с сайта OpenWeatherMap, который предоставляет данные о погоде.

Регистрация на сайте OpenWeatherMap:

Переходим на сайт и нажмите на кнопку "Sign In".
Выбираем раздел "Create Account".
Вводим имя пользователя, почту и пароль (дважды).
Поставим галочки в обязательных полях и пройдем проверку на робота.
Нажимаем "Create Account" и подтверждаем почту, перейдя по ссылке в письме.
После подтверждения почты получаем доступ к аккаунту и API-ключу, который будем использовать для запросов к API.

Получение API-ключа

Для работы с API нам потребуется токен (API-ключ):

В своём аккаунте OpenWeatherMap заходим в раздел My API keys
____
Перед началом работы пропишем логику и начнём с Flask, который понадобится для Backend приложения.

#импортируем Flask и библиотеку Request
from flask import Flask, render_template, request
import requests

#импортируем объект класса Flask
app = Flask(__name__)

#формируем путь и методы GET и POST
@app.route('/', methods=['GET', 'POST'])
#создаем функцию с переменной weather, где мы будем сохранять погоду
def index():
   weather = None
#формируем условия для проверки метода. Форму мы пока не создавали, но нам из неё необходимо будет взять только город.   
   if request.method == 'POST':
#этот определенный город мы будем брать для запроса API
       city = request.form['city']
   return render_template("index.html")
Создаём папку templates на боковой панели, а внутри создаём файл html:


Функцияя index не взаимодействует с API, поэтому следующим шагом мы пропишем функцию, которая будет взаимодействовать с API и брать информацибю о погоде.

Для начала зайдём на сайт OpenWeatherMap в раздел My API keys и копируем свой ключ.

#в функции прописываем город, который мы будем вводить в форме
def get_weather(city):
   api_key = "ваш_ключ"
   #адрес, по которомы мы будем отправлять запрос. Не забываем указывать f строку.
   url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
   #для получения результата нам понадобится модуль requests
   response = requests.get(url)
   #прописываем формат возврата результата
   return response.json()
Для поиска адреса на сайте OpenWeatherMap необходимо перейти в раздел Встроенный API-запрос по названию города и скопировать url вызова API:

___
Дополняем функцию index, чтобы запросить погоду по определённому городу.

from flask import Flask, render_template, request
import requests


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
   weather = None
   if request.method == 'POST':
       city = request.form['city']
       #прописываем переменную, куда будет сохраняться результат и функцию weather с указанием города, который берем из формы
       weather = get_weather(city)
       #передаем информацию о погоде в index.html
   return render_template("index.html", weather=weather)
Прописываем запуск для проверки приложения

if __name__ == '__main__':
   app.run(debug=True)
Заполняем файл index.html

<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <title>Title</title>
   
</head>
<body>
<h1>Сайт с прогнозом погоды в любой точке мира</h1>
   
#создаём форму для запроса
<form method="post">
    <input type="text" name="city" placeholder="Введите город" required>
    <button type="submit">Узнать погоду</button>
   </form>

   #получение информации
   <div class="result">
   #условия для вывода информации
       {% if weather %}
           #подставляем значение, которое передается в переменной weather и ключи, который берём из результата с сайта OpenWeatherMap 
           <h3>Погода в {{ weather['name'] }}</h3>
           <p>Температура: {{ weather['main']['temp'] }}°C</p>
           <p>Погода: {{ weather['weather'][0]['description'] }}</p>
       {% endif %}
</div>
</body>
</html>
placeholder — атрибут, который показывает, что будет неаписано внутри поля.

Отправляем код в Нейрокота и формируем запрос: Оформи красиво данный сайт с использованием bootstrap.
Таким образом, мы получили красивый и отформатированный результат:

<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <meta name="viewport" content="width=device-width, initial-scale=1">
   <title>Прогноз погоды</title>
   <!-- Bootstrap CSS -->
      <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
<div class="container mt-5">
   <h1 class="text-center mb-4">Сайт с прогнозом погоды в любой точке мира</h1>
   #создаём форму для запроса
   <form method="post" class="form-inline justify-content-center mb-4">
       <div class="form-group mx-sm-3 mb-2">
           <input type="text" class="form-control" name="city" placeholder="Введите город" required>
       </div>
       <button type="submit" class="btn btn-primary mb-2">Узнать погоду</button>
   </form>

   <div class="result text-center"
       {% if weather %}
           <h3>Погода в {{ weather['name'] }}</h3>
           <p>Температура: {{ weather['main']['temp'] }}°C</p>
           <p>Погода: {{ weather['weather'][0]['description'] }}</p>
       {% endif %}
   </div>


   <div class="result text-center">


       {% if news %}
           <h2>Новости:</h2>
           <ul>
               {% for article in news %}
                   <li><a href="{{ article['url'] }}"> {{ article['title'] }} </a></li>
               {% endfor %}
           </ul>
       {% endif %}


   </div>
</div>


<!-- Bootstrap JS and dependencies -->
<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.3/dist/umd/popper.min.js"></script>
Возвращаемся во вкладку main.py и проверяем результат. Информация о температуре указана в Кельвинах. Для того, чтобы это исправить на сайте OpenWeatherMap необходимо перейти в раздел Меры измерения и из url для вызова API скопировать необходимую часть: &units=metric

Добавляем её в функцию:

def get_weather(city):
   api_key = "ваш_ключ"
   url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
   response = requests.get(url
   return response.json()
____________________________________________________________________________
Используем NewsAPI — она нужна, чтобы мы могли получать новости.

Мы будем получать новости и выводить их на сайте.

Переходим на сайт newsapi.org.
Нажимаем на кнопку Get API Key.
Регистрируемся: вводим имя, адрес электронной почты, придумываем пароль, выбираем свой статус использования АПИ (человек или компания), ставим галочку о том, что не являемся роботом, нажимаем на кнопку Submit.
Копируем API-ключ.
Переходим в PyCharm.
Создаём переменную для получения новостей и вставляем ключ:
def get_news():
   api_key = "a617b533135849c1b9cf361a6b4b84ea"
7. Возвращаемся на страницу с ключом, нажимаем на getting started guide.

8. На панели слева переходим в раздел Get curated breaking. Справа копируем адрес ссылки.

9. Возвращаемся в PyCharm и продолжаем код — вставляем адрес в новую переменную:

def get_news():
   api_key = "a617b533135849c1b9cf361a6b4b84ea"
   url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
10. Прописываем отправку запроса по данному адресу и получение json:

def get_news():
   api_key = "a617b533135849c1b9cf361a6b4b84ea"
   url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
   response = requests.get(url)
   return response.json()
11. Возвращаемся на страницу с гайдом. Справа находим список по ключу articles. Это список статей, новостей. Нам нужно получать список с новостями.

12. Возвращаемся в PyCharm и продолжаем код — дополняем получение новостей, вводим ключ. Если ключа не будет, возвращаться будет пустой список.

def get_news():
   api_key = "a617b533135849c1b9cf361a6b4b84ea"
   url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
   response = requests.get(url)
   return response.json().get('articles', [])
13. Дополняем код в блоке выше, создаём переменную для вызова результата работы функции:

@app.route('/', methods=['GET', 'POST'])
def index():
   weather = None
   news = None
   if request.method == 'POST':
       city = request.form['city']
       weather = get_weather(city)
       news = get_news()
   return render_template("index.html", weather=weather, news=news)
14. Дополняем код в HTML-документе, чтобы видеть информацию о новостях. Создаём блок-условие с заголовком под тегом <h2>:

<div class="result text-center">
       {% if weather %}
           <h3>Погода в {{ weather['name'] }}</h3>
           <p>Температура: {{ weather['main']['temp'] }}°C</p>
           <p>Погода: {{ weather['weather'][0]['description'] }}</p>
       {% endif %


       {% if news %}
           <h2>Новости:</h2>

       {% endif %}


   </div>
15. Создаём тег <ul>, чтобы отобрать новости списком.

{% if news %}
           <h2>Новости:</h2>
           <ul>

           </ul>
       {% endif %}
16. Создаём цикл for, чтобы перебирать новости внутри news. Прописываем тег <li> для того, чтобы новости отображались элементами списка. С сайта берём ключ url, внутри которого содержится ссылка на новость. Помещаем ключ внутри тега href:

{% if news %}
           <h2>Новости:</h2>
           <ul>
               {% for article in news %}
                   <li><a href="{{ article['url'] }}"> {{ article['title'] }} </a></li>
               {% endfor %}
           </ul>
       {% endif %}
С помощью цикла for мы будем перебирать каждую из наших новостей, каждую новость будем сохранять в переменную article, далее будем вставлять ссылку и заголовок новости.

17. Создаём дополнительный блок, чтобы сайт выглядел более красиво и имел правильное разделение:

<div class="result text-center">


       {% if news %}
           <h2>Новости:</h2>
           <ul>
               {% for article in news %}
                   <li><a href="{{ article['url'] }}"> {{ article['title'] }} </a></li>
               {% endfor %}
           </ul>
       {% endif %}


   </div>
