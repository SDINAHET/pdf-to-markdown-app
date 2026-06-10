Test

Rebuild l’image :
```bash
docker compose build --no-cache pdf-to-md-tests
```

Lancement des test:
```bash
docker compose --profile test run --rm pdf-to-md-tests
```

Build et test en une commande:
```bash
docker compose --profile test run --rm --build pdf-to-md-tests
```

resultats des tests en html en couleur:
```bash
docker compose --profile test run --rm pdf-to-md-tests pytest --cov=app --cov-report=html --cov-report=term-missing --cov-fail-under=80
```


```bash
root:/mnt/c/Users/Stéphane_HP
/Documents/projet pdf to md/pdf-to-markdown-app$ docker compose --profile test run --rm pdf-to-md-tests
Container pdf-to-markdown-app-pdf-to-md-tests-run-e31413c653be Creating
Container pdf-to-markdown-app-pdf-to-md-tests-run-e31413c653be Created
============ test session starts =============
platform linux -- Python 3.12.13, pytest-9.0.3, pluggy-1.6.0
rootdir: /app
plugins: cov-7.1.0, anyio-4.13.0
collected 16 items

tests/test_app.py ................     [100%]

============== warnings summary ==============
../usr/local/lib/python3.12/site-packages/fastapi/testclient.py:1
  /usr/local/lib/python3.12/site-packages/fastapi/testclient.py:1: StarletteDeprecationWarning: Using `httpx` with `starlette.testclient` is deprecated; install `httpx2` instead.
    from starlette.testclient import TestClient as TestClient  # noqa

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=============== tests coverage ===============
_ coverage: platform linux, python 3.12.13-final-0 _

Name     Stmts   Miss  Cover   Missing
--------------------------------------
app.py      38      3    92%   65, 91, 99
--------------------------------------
TOTAL       38      3    92%
Required test coverage of 80% reached. Total coverage: 92.11%
======= 16 passed, 1 warning in 5.71s ========
root:/mnt/c/Users/Stéphane_HP
/Documents/projet pdf to md/pdf-to-markdown-app$
```

```bash
explorer.exe "./backend/htmlcov/index.html"
```
--> ne fonctionne pas ici!
