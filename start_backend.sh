git fetch && git pull
pipenv shell
pipenv install --dev
export PYTHONPATH=$PWD
python3 app/initial_data.py
uvicorn app.main:app --reload