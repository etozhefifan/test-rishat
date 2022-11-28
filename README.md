## How to install and check project locally

To install:
1. Clone the repository
```
git clone {ssh}
```
2. Create a virtual environment to store all dependencies:
```
python -m venv .venv
```
And then activate env:
```
.venv/scripts/activate
(for windows users)
. .venv/bin/activate
(for linux)
```
3. Install all dependencies from requirements.txt
```
pip install -r requirements.txt
```
4. Run server:
```
python manage.py runserver
```