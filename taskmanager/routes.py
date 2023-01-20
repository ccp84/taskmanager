from flask import render_template
from taskmanager import app, db
from taskmanager.models import Task, Category


@app.route("/")
def home():
    return render_template("tasks.html")


@app.route("/categories")
def categories():
    return render_template("categories.html")
