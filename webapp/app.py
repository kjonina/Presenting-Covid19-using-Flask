from flask import Flask, render_template

app = Flask(__name__)



@app.get("/")
def show_page1():
    return render_template("home_page.html")


if __name__ == "__main__":  # Will eval to False when this code imported.
    app.run(debug=True)
