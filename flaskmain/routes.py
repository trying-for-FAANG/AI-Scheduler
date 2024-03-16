from flask import Flask, render_template, url_for, flash, redirect, request
from flaskmain import application

@application.route("/")
@application.route("/home")
def home():
    return render_template("index.html", title = "Home")