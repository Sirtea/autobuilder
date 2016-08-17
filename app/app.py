from flask import Flask, render_template
from models import Fruit

app = Flask(__name__)


@app.route('/')
def list_fruits():
    return render_template('list_fruits.html', fruits=Fruit.objects())
