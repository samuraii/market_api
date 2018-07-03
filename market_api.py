import requests

VERSION = 'v2'
URL = 'https://api.content.market.yandex.ru/v2'

def api_key():
	with open('key', 'r') as key:
		return key.read()

def get_categories(version=VERSION, url=URL):
	headers = {'Authorization': api_key()}
	params = {'geo_id': 213, 'name_part': 'moc'}
	r = requests.get(URL + '/categories', headers=headers, params=params)
	print(r.json())

get_categories()