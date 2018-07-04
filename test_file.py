import pytest
import market_api as ma


def test_invalid_authorization_key():
	result = ma.get_from_api(what='/categories', key='invalid-api-key')
	assert result.status_code == 401, 'Сервер не ответил 401 на передачу неправильного ключа авторизации'


def test_without_required_params():
	result = ma.get_from_api(what='/categories', params={})
	assert result.status_code == 422, 'Сервер не ответил 422 на запрос без необходимиых параметров'