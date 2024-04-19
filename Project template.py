from flask import Flask, render_template
import sqlite3
import pathlib
import os

base_path = pathlib.Path(__file__).parent
db_name = "Housing.db"
db_path = base_path / db_name
print(db_path)
print(db_path)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index_links.html") 

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/data")
def data():
    con = sqlite3.connect(db_path)
    cursor = con.cursor()
    housing_prices11 = cursor.execute("SELECT * FROM housing_prices11").fetchall()
    con.close()

    return render_template("data_table.html", housing_prices11=housing_prices11)

if __name__=="__main__":
    app.run(debug=True)