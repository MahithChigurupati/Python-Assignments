import requests,bs4

def weather(city):
    city=city.replace(' ','-')
    city=city.title()
    print(city)
    url=f'https://www.weather-forecast.com/locations/{city}/forecasts/latest'
    res=requests.get(url)
    soup=bs4.BeautifulSoup(res.text,'lxml')
    soup=soup.select('td')
    print(soup[0].text)


if __name__ == '__main__':
  city = input(' Enter your city')
  weather(city)
