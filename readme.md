# Projekt Hollymovies

## Sylabus
### 27. května 2025
- Úvod
- Vytvoření projektu
- Vytvoření superuser

## Django
### Instalace
```bash
pip install django
pip freeze > requirements.txt
django-admin startproject <nazev_projektu> .
```

### Struktura projektu
- `hollymovies` - složka projektu (obsahuje informace o celém projektu)
  - `__init__.py` - je zde jen proto, aby daná složka byla package
  - `asgi.py` - nebudeme potřebovat
  - `settings.py` - nastavení projektu
  - `urls.py` - zde jsou nastavené url adresy
  - `wsgi.py` - nebudeme potřebovat
- `manage.py` - hlavní skript pro práci s projektem (souštění serveru, testů, migrací,...)

### Spuštění serveru
```bash
python manage.py runserver
```

### .env
Slouží k ukládání citlivých informací (SECRET_KEY, hesla, přístupové údaje,...).

#### Instalace
```bash
pip install python-dotenv
pip freeze > requirements.txt
```

Vytvoříme soubour s názvem `.env` v kořenovém adresáři projektu.

Do souboru `settings.py` vložíme:
```python
from dotenv import load_dotenv
load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY', default='django-insecure-)si+fpno3#)=7__vx-4%ni^&n1wvaz9bju1e+s8*i!e9qt!@f)')
```

### .gitignore
Správný projekt má nastavení pro ingorované soubory v git repozitáři v souboru `.gitignore`.
```git
/.idea
*.pyc
/db.sqlite3
/.env
```

### Aplikace
#### Vytvoření
```bash
python manage.py startapp <název_aplikace>
```

#### Struktura aplikace
- `viever` - složka aplikace
  - `migrations` - složka obsahující migrační skripty
  - `__init__.py` - je tu zde jen proto, aby daná složka byla package
  - `admin.py` - nastavení administrační stránky
  - `apps.py` - nastavení aplikace - nebudeme upravovat
  - `models.py` - zde bude definice modelů (databáze)
  - `tests.py` - zde budou testy
  - `views.py` - zde budou views (funkcionalita)

#### Registrace aplikace
Do souboru `settings.py` musíme novou aplikaci zaregistrovat do seznamu 
`INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'viewer',
]
```

## Publikování projektu na GitHub
- V PyCharm: Main menu -> Git -> GitHub -> Share Project on GitHub
- můžete změnit název repozitáře
- Na GitHub
  - nasdílet kód repozitáře
  - Settings -> Colloborators -> Add people 

### Vytvoření superuživatele
```bash
python manage.py createsuperuser
```

# Práces GITem
- `master` - hlavní branch (větev) - zde nikdy neprogramujeme, slouží k tzv. release
- `dev` - hlavní vývojová větev - slouží k rozdělování práce do jednolivých pracovních větví. Ani zde
neprogramujeme.
- `feature-branches` - vývojové větve, které vycházejí z `dev`. Pro každou novou funkcionalitu
vytváříme samostanou vývojovou větev. Zde programujeme danou funkcionalitu, otestujeme a
až když je plně funkční, provedeme `merge` do větve `dev`. Ve větvi `dev` vše znovu otestuji 
(mohlo dojít ke konfliktu a mohlo se tedy něco "rozbít"). Pokud je i zde vše funkční, můžeme dát
`merge` do `master`.