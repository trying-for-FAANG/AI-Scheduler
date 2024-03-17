from flask import Flask

application = Flask(__name__)
application.config["SECRET_KEY"] = "wlUukJvvSQIQf30pu4umLA"


from flaskmain import routes
