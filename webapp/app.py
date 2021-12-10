from flask import Flask, render_template

from plotly_plots import create_covid_graph
from tidy_data import create_csv

df = create_csv()  # global. Runs on restart - may lead to stale data

app = Flask(__name__)

@app.get("/")
def show_home():
    return render_template("home_page.html")


@app.get("/assignment")
def show_assignment():

    return render_template("assignment_page.html", graph1  = create_covid_graph(df))


if __name__ == "__main__":  # Will eval to False when this code imported.
    app.run(debug=True)
