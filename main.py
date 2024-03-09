from flask import Flask, render_template
# flask has templates and static folder structure
# inside templates index.html file and images, css, jscript files in static
# now create app instance with Flask class

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
app.run(debug=True, port=5001)