# Чеклист для проверки API Яндекс Маркет (раздел "Категории", для версии "v2")
## https://tech.yandex.ru/market/content-data/doc/dg-v2/reference/category-controller-v2-get-root-categories-docpage/

1) Проверка доступа к API с невалидным значением ключа. `Atomated`

2) Проверка доступа к API с валидным значением ключа и необходимыми параметрами. `Automated`

3) Проверка доступа к API с валидным значением ключа и отсуствием необходимых параметров. `Automated`

4) Проверка работоспособности парамтера fields (fields: STATISTICS, PARENT, WARNINGS) `Partly Automated`

5) Проверка работоспособности парамтера format (format: JSON, XML) `Automated`

6) Проверка типов данных в ответе сервера в соотвествии со схемой данных в документации. `Partly Automated`
