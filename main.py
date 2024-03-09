from datetime import datetime
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

# flask has templates and static folder structure
# inside templates index.html file and images, css, jscript files in static
# now create app instance with Flask class
app = Flask(__name__)

app.config["SECRET_KEY"] = "myapplication123"
# this is a dictionary, it is a secret key which protect from hackers etc
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
# this is the db name and db type (sqlite) used to create
db = SQLAlchemy(app)


# create a database, to create it we need a model
class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    date = db.Column(db.Date)
    occupation = db.Column(db.String(80))



@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name  = request.form["last_name"]
        email = request.form["email"]
        date = request.form["date"]
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        occupation = request.form["occupation"]

        form = Form(first_name=first_name, last_name=last_name,
                    email=email, date=date_obj, occupation=occupation)
        db.session.add(form)
        db.session.commit() # this add data to db
    return render_template("index.html")


if __name__ =="__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True, port=5001)
