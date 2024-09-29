# Card Explorer
My attempt at creating a website for searching for Lorcana cards and making decks.

## Setup
1. Clone repo
```
git clone https://github.com/zishiwu123/cardexplorer.git
```

2. Create virtualenv
```
cd backend
python3 -m venv .venv
```

3. Activate virtualenv
- Windows
```
source .venv/Scripts/activate
```

- MacOS/Linux
```
source .venv/bin/activate
```

4. Install dependencies
```
pip install -r requirements.txt
```

5. Run tests
```
python -m unittest discover
```

6. Run API on localhost:8000
```
cd backend
python main.py
```
