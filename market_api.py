import requests

def api_key():
	with open('key.txt', 'r') as key:
		return key.read()

def get_from_api(what='/categories', key=api_key(), params={'geo_id': 213, 'name_part': 'moc'}):
	headers = {'Authorization': key}
	r = requests.get('https://api.content.market.yandex.ru/v2' + what, headers=headers, params=params)
	return r
