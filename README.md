# RYM
# A flask application for Responsible Young Men

# This application is designed to run locally.
# It uses sqlalchemy for the database and need to be stup locally for the application to run smoothly.
# Run the following on your terminal to setup the database(linux)
export FLASK_APP=main

# For windows
set FLASK_APP=main

# Below is for both OS

flask shell

# Run these commands after the python shell is opend

from main import models 
from main.models import db
db.create_all()
exit()
