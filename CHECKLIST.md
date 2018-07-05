# Чеклист для проверки API Яндекс Маркет (раздел "Категории", для версии "v2")
## https://tech.yandex.ru/market/content-data/doc/dg-v2/reference/category-controller-v2-get-root-categories-docpage/

Auto 1) Проверка доступа к API с невалидным значением ключа.

Auto 2) Проверка доступа к API с валидным значением ключа и необходимыми параметрами.

Auto 3) Проверка доступа к API с валидным значением ключа и отсуствием необходимых параметров.

Partly Automated 4) Проверка работоспособности парамтера fields (fields: STATISTICS, PARENT, WARNINGS)

Auto 5) Проверка работоспособности парамтера format (format: JSON, XML)

Partly Automated 6) Проверка типов данных в ответе сервера в соотвествии со схемой данных в документации.