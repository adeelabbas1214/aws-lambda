import requests
class API():
    def api_weather(self, city):
        url = f'https://wttr.in/{city}'
        response = requests.get(url)
        print(response.text)
api_a = API()
api_a.api_weather('Islamabad')


