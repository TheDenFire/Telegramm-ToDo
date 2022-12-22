BOT_API_TOKEN = '5717622433:AAGxWsBsH1dVCBD3xmyI5c3ON97bj9q-XgU'
WEATHER_API_KEY = '8537d9ef6386cb97156fd47d832f479c'

CURRENT_WEATHER_API_CALL = (
        'https://api.openweathermap.org/data/2.5/weather?'
        'lat={latitude}&lon={longitude}&'
        'appid=' + WEATHER_API_KEY + '&units=metric'
)