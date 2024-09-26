# Activate virtualenv for different OS
if [ "$(expr substr $(uname -s) 1 10)" == "MINGW32_NT" ]; then
    # Do something under 32 bits Windows NT platform
    source .venv/Scripts/activate
elif [ "$(expr substr $(uname -s) 1 10)" == "MINGW64_NT" ]; then
    # Do something under 64 bits Windows NT platform
    source .venv/Scripts/activate
else
    # Assume MacOS or Linux
    source .ven/bin/activate
fi

cd cardexplorer
fastapi dev main.py
