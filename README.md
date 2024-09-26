# Card Explorer
My attempt at creating a website for searching for Lorcana cards and making decks.

## Setup
1. Clone repo
```
git clone https://github.com/zishiwu123/cardexplorer.git
```

2. Create virtualenv
```
cd cardexplorer
python3 -m venv .venv
```

3. Activate virtualenv
- Windows
```
source .venv/Scripts/activate
```

- MacOS/Linux
```
source .ven/bin/activate
```

4. Install dependencies
```
pip install -r requirements.txt
```

5. Run app
```
cd cardexplorer
fastapi dev main.py
```