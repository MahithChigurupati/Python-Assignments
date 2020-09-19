from urllib.request import urlopen
import json

def find_ip():
    data=urlopen('https://ipinfo.io/')
    data=json.load(data)
    return (data['ip'], data['city'])


if __name__ == '__main__':
    data = find_ip()
    print(f'your ip adress is: {data[0]}\nyour city is: {data[1]}')
