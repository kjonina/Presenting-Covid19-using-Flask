from flask import Flask, render_template

app = Flask(__name__)


@app.get("/")
def hello():
    return "Hello from my first Flask webapp with debugging."


@app.get("/page1")
def show_page1():
    return render_template("page1.html", title="This is page 1")


@app.get("/page2")
def show_page2():
    return render_template("page2.html", title="This is page 2")


@app.get("/page3")
def show_page3():
    return render_template("page3.html", title="This is page 3")


if __name__ == "__main__":  # Will eval to False when this code imported.
    app.run(debug=True)
