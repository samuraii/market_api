import pytest
import market_api as ma
import xml.etree.ElementTree as ET

# Cache parametr, required to eliminate extra requests
json_data = None


def test_invalid_authorization_key():
	result = ma.get_from_api(what='/categories', key='invalid-api-key')
	assert result.status_code == 401, 'Сервер не ответил 401 на передачу неправильного ключа авторизации'


def test_without_required_params():
	result = ma.get_from_api(what='/categories', params={})
	assert result.status_code == 422, 'Сервер не ответил 422 на запрос без необходимиых параметров'


def test_valid_request_params_and_key():
	result = ma.get_from_api(what='/categories')
	assert result.status_code == 200, 'Сервер не ответил 200 на запрос с валидными параметрами'


def test_json_request_param():
	global json_data # Cache
	result = ma.get_from_api(what='/categories', params={'geo_id': 213, 'name_part': 'moc', 'format': 'JSON'})
	assert result.status_code == 200, 'Сервер не ответил 200 на запрос с валидными параметрами'
	assert result.json()['status'] == 'OK', 'Результат status запроса формата JSON не соотвествует ожидаемому. Проверьте корректность ответа.'
	if json_data is None:
		json_data = result.json()


def test_xml_request_param():
	result = ma.get_from_api(what='/categories', params={'geo_id': 213, 'name_part': 'moc', 'format': 'XML'})
	assert result.status_code == 200, 'Сервер не ответил 200 на запрос с валидными параметрами'
	root = ET.fromstring(result.text)
	assert root.findall('.')[0].get('status') == 'OK', 'Результат status запроса формата XML не соотвествует ожидаемому. Проверьте корректность ответа.'


def test_params_data_from_request():
	global json_data
	assert int(json_data['context']['region']['id']) == 213, 'Значение id региона не соотвествует ожидаемому'
	assert str(json_data['context']['region']['name']) == 'Москва', 'Значение name региона не соотвествует ожидаемому'
	assert int(json_data['context']['region']['country']['id']) == 225, 'Значение country id региона не соотвествует ожидаемому'
	assert str(json_data['context']['region']['country']['name']) == 'Россия', 'Значение country name региона не соотвествует ожидаемому'


def test_fields_param_on_json():
	global json_data # Cache
	result = ma.get_from_api(what='/categories', params={'geo_id': 213, 'name_part': 'moc', 'fields': 'STATISTICS'})
	assert result.status_code == 200, 'Сервер не ответил 200 на запрос с валидными параметрами'
	assert result.json()['status'] == 'OK', 'Результат status запроса формата JSON не соотвествует ожидаемому. Проверьте корректность ответа.'
	assert int(list(result.json()['categories'])[0]['modelCount']), 'Неверный формат, либо отсуствует аттрибут modelCount при запросе с параметром STATISTICS'
