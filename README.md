# Yandex Market Api testing

This repo contains tests for API interface of yandex.market.

Doc: https://tech.yandex.ru/market/content-data/doc/dg-v2/reference/category-controller-v2-get-category-docpage/

# Requiremetns

python <3.6

API Key for Yandex Market (should be placed in key file)

# Checklist

The full checkist can be found [HERE](https://github.com/samuraii/market_api/blob/master/CHECKLIST.md)

# How to launch tests

1) Clone this repo to local computer

2) [Virtual environment](https://docs.python.org/3/library/venv.html) based on python 3.6 is recommended to use:

2.1) Create virtual env:
```bash
python -m venv env
```

2.2) Activate virtual env:

_Windows (Powershell)_
```bash
env\Scripts\activate.ps1
```
_Mac OS_
```bash
source env/bin/activate
```

3) Install requirements
```bash
pip install -r requirements.txt
```

4) Run tests
```bash
pytest --html=report.html
```

5) Open report.html to see the results
