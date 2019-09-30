# app_gestion_immobiliere

# Setup

```bash
virtualenv -p python2.7 .env27
source .env27/bin/activate
pip install -r requirements.txt
```

# Init database and Launch

```bash
source .env27/bin/activate
python main.py init_db
```

# Regular use

```bash
source .env27/bin/activate
python main.py
```

# Before deploying prod

- Change the db key in main.cfg
- Disable debug mode in main.py

# Test

```bash
python tests.py
```
