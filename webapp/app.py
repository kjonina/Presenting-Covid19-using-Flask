from flask import Flask, render_template

from plotly_plots import graph1,graph2, graph2_extra, graph3, graph3_extra, graph4, graph5
from tidy_data import create_csv
from new_df import create_new_dfs



app = Flask(__name__)



df = create_csv()  # global df

aged_df, hospitalised_df, aged_and_hospitalised_df, confirmed_cc_df, hospital_cc_df, icu_cc_df,  median_age_df = create_new_dfs(df) # creating global other dfs


@app.get("/")
def show_home():
    return render_template("home_page.html")

@app.get("/graph1")
def show_graph1():
    return render_template("graph1.html", graph1 = graph1(confirmed_cc_df, hospital_cc_df,icu_cc_df))

@app.get("/graph2")
def show_graph2():
    return render_template("graph2.html", graph2  = graph2(aged_df), graph2_extra = graph2_extra(hospitalised_df))

@app.get("/graph3")
def show_graph3():
    return render_template("graph3.html", graph3 = graph3(aged_df), graph3_extra = graph3_extra(hospitalised_df))

@app.get("/graph4")
def show_graph4():
    return render_template("graph4.html", graph4 = graph4(confirmed_cc_df, median_age_df))

@app.get("/graph5")
def show_graph5():
    return render_template("graph5.html", graph5 = graph5(aged_df, hospitalised_df))

if __name__ == "__main__":
    app.run(debug=True)
