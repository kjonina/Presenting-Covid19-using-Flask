from flask import Flask, render_template

app = Flask(__name__)

# =============================================================================
# Importing functions from other files
# =============================================================================
from plotly_plots import graph1,graph2, graph2_extra, graph3, graph3_extra, graph4, graph5
from tidy_data import create_csv
from new_df import create_new_dfs

# =============================================================================
# Creating dfs
# =============================================================================
# crating a global df so that the when each page is loaded, the dataset is already created and speeds up the process
df = create_csv()

# crating a global dfs so that the when each page is loaded, the dataset is already created and speeds up the process
aged_df, hospitalised_df, aged_and_hospitalised_df, confirmed_cc_df, hospital_cc_df, icu_cc_df,  median_age_df = create_new_dfs(df)

# =============================================================================
# Graph Pages
# =============================================================================
# home page
@app.get("/")
def show_home():
    return render_template("home_page.html")

# graph1
@app.get("/graph1")
def show_graph1():
    return render_template("graph1.html", graph1 = graph1(confirmed_cc_df, hospital_cc_df,icu_cc_df))

# graph2
@app.get("/graph2")
def show_graph2():
    return render_template("graph2.html", graph2  = graph2(aged_df), graph2_extra = graph2_extra(hospitalised_df))

# graph3 - TAKES A WHILE TO LOAD!!!
@app.get("/graph3")
def show_graph3():
    return render_template("graph3.html", graph3 = graph3(aged_df), graph3_extra = graph3_extra(hospitalised_df))

# graph4
@app.get("/graph4")
def show_graph4():
    return render_template("graph4.html", graph4 = graph4(confirmed_cc_df, median_age_df))

# graph5
@app.get("/graph5")
def show_graph5():
    return render_template("graph5.html", graph5 = graph5(aged_df, hospitalised_df))

# =============================================================================
# A Single Page
# =============================================================================
# a single page was developed with appropriate javascript on the assignement_page
# however it took WWWWWAAAAAAAAAAYYYYYYYYYY to long to load
# because of all the graphs that had to be loaded and hidden
# and the animation in graph 3 starts playing although the play button was not clicked
# so that made the website really slow and unresponsive.
# Instead, 5 pages dedicated to each graphs were decided upon.

@app.get("/assignment")
def show_assignment():
    return render_template("assignment_page.html", graph1 = graph1(confirmed_cc_df, hospital_cc_df,icu_cc_df),
                                                    graph2  = graph2(aged_df),
                                                    graph2_extra = graph2_extra(hospitalised_df),
                                                    graph3 = graph3(aged_df),
                                                    graph3_extra = graph3_extra(hospitalised_df),
                                                    graph4 = graph4(confirmed_cc_df, median_age_df),
                                                    graph5 = graph5(aged_df, hospitalised_df))

# =============================================================================
# Runs when the app is run
# =============================================================================
if __name__ == "__main__":
    app.run(debug=True)
