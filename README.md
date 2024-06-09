# RYM
A flask application for Responsible Young Men

This application is designed to run locally.
It uses sqlalchemy for the database and need to be stup locally for the application to run smoothly.
If you don't have flask installed, run "sudo apt install python3-flask" on linux systems or "Pip install flask on both windows and Unix systems"

**Run the following on your terminal to setup the database(linux)**
`export FLASK_APP=main`

**For windows**
`set FLASK_APP=main`

# Below is general for all operating systems 

flask shell

- Run these commands after the python shell is opend
```py
from main import models 
from main.models import db
db.create_all()
exit()
```
