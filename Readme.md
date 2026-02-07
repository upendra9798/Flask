python -m virtualenv env  -> Making a virtual environment for python
.\env\Scripts\activate.ps1 - Activating this env ->Entered in env file
pip install flask (in env) (in venv)

Static -> In Flask, the static folder is used to store static files — files that don’t change on the server and are sent directly to the browser.

For Database -> pip install flask-sqlalchemy (We can make changes in database by python)
(.\.venv\Scripts\activate
pip install flask-sqlalchemy) - Have to install in venv

To run -> 1->  .\env\Scripts\activate.ps1 (enter in env)
          2->  python .\app.py


This will properly set up the context and allow db.create_all() to work:-
from app import app, db
with app.app_context():
    db.create_all()


FOR DEPLOYMENT 
    (in env)
    pip install gunicorn
    pip freeze > requirements.txt