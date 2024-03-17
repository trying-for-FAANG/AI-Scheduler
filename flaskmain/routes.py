from flask import Flask, render_template, url_for, flash, redirect, request
from flaskmain import application
from flaskmain.forms import SubmitForm

@application.route("/", methods = ["GET", "POST"])
@application.route("/home", methods = ["GET", "POST"])
def home():
    form = SubmitForm()
    if form.validate_on_submit():
        print("okay")
    if request.method == 'POST':
        selected_major = request.form["major"]
        semester = request.form["semester"]
        message = request.form["message"]
        # Process the selected major as needed
        print(selected_major)
        list = []
        list.append(selected_major)
        list.append(semester)
        list.append(message)
        return f'Selected major: {list}'
    
    return render_template("index.html", title = "Home", form = form)