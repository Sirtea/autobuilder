#!/bin/bash

PYTHONDONTWRITEBYTECODE=" " \
PYTHONPATH="app" \
FLASK_APP="app:app" \
MONGODB_URI="mongodb://localhost:27017/shop" \
./env/bin/flask run --debugger --reload
