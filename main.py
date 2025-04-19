from flask import Flask, render_template, request
import requests
from datetime import datetime

app = Flask(__name__)  # Исправлено: заменено name на __name__

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    news = None
    if request.method == 'POST':
        city = request.form['city']
        weather = get_weather(city)
        news = get_news()
    return render_template('index.html', weather=weather, news=news)

def get_weather(city):
    api_key = 'b149289ce44b6b00078777e1b8a1aa02'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_news():
    api_key = '46709867aedf4f9e94fcd34a691e9f35'
    today = datetime.today().strftime('%Y-%m-%d')
    url = f"https://newsapi.org/v2/everything?q=Apple&from={today}&sortBy=popularity&apiKey={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json().get('articles', [])
    else:
        print(f"Error fetching news: {response.status_code}")  # Отладка
        return []

if __name__ == '__main__':  # Исправлено: заменено name на __name__
    app.run(debug=True)


