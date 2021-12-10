from flask import Flask, render_template

app = Flask(__name__)

@app.get("/")
def show_home():
    return render_template("home_page.html")


@app.get("/assignment")
def show_assignment():
    return render_template("assignment_page.html")


if __name__ == "__main__":  # Will eval to False when this code imported.
    app.run(debug=True)
