# Backend technologies

## Sylabus
### Úterý, 27. května · 17:30–21:00
- Prošli jsme slidy 1-15 
- Úvod
- Vytvoření projektu `hollymovies`
- Vytvoření superuser
- Vytvoření aplikace `viewer`
- .env
- Git repozitář (.gitignore)
- readme.md
- Domácí úkol: definovat add2 funkci pro sčítání pomocí kódování URL

### Středa, 28. května · 17:30–21:00
### Pátek, 30. května · 17:30–21:00
### Pondělí, 2. června · 17:30–21:00
### Úterý, 3. června · 17:30–21:00
### Čtvrtek, 5. června · 17:30–21:00
### Pátek, 13. června · 17:30–21:00
### Pondělí, 16. června · 17:30–21:00
### Středa, 25. června · 17:30–21:00
### Pondělí, 30. června · 17:30–20:30
### Úterý, 1. července · 17:30–21:00
### Čtvrtek, 3. července · 17:30–21:30

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
- `viewer` - složka aplikace
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

# Projekt Hollymovies
## Funkcionalita
- [ ] 1 seznam filmů (abecedně)
- [ ] 2 detail filmu 
  - [ ] originální název
  - [ ] český název
  - [ ] režisér
  - [ ] herci
  - [ ] skladatel hudby
  - [ ] délka
  - [ ] popis
  - [ ] rok
  - [ ] země
  - [ ] hodnocení
  - [ ] ocenění
  - [ ] obrázky
  - [ ] návštěvnost v kinech (https://kinomaniak.cz/)
  - [ ] VOD (https://www.kinobox.cz/)
  - [ ] žánr
  - [ ] trailer
  - [ ] kde se odehrává film
- [ ] 3 filtrování filmů
  - [ ] podle žánru 
  - [ ] podle roku
  - [ ] podle hodnocení
  - [ ] podle herce
- [ ] 4 seznam herců
- [ ] 5 detail herce
  - [ ] jméno
  - [ ] příjmení
  - [ ] umělecké jméno
  - [ ] filmy, ve kterých hrál
  - [ ] datum narození
  - [ ] datum úmrtí
  - [ ] země
  - [ ] ocenění
  - [ ] biografie
  - [ ] obrázky

## Databáze
- [x] Genre
  - [x] name (String)
- [ ] Country
  - [ ] name (String) 
- [ ] Creator
  - [ ] name (String)
  - [ ] surname (String)
  - [ ] artistic_name (String)
  - [ ] date_of_birth (Date)
  - [ ] date_of_death (Date)
  - [ ] country (FK -> Country)
  - [ ] biography (String)
- [ ] Movie
  - [ ] title_orig (String)
  - [ ] title_cz (String)
  - [ ] genres (n:m -> Genre)
  - [ ] directors (n:m -> Creator)
  - [ ] actors (n:m -> Creator)
  - [ ] composers (n:m -> Creator)
  - [ ] length (Integer) (minuty)
  - [ ] description (String)
  - [ ] year (Integer)
  - [ ] countries (n:m -> Country)