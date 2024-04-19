from flask import Flask, render_template
import sqlite3
import pathlib 

base_path = pathlib.Path(r'C:\Users\91939\OneDrive\Documents\DAB111\.venv\Project\Housing.db')
db_name = "Housing.db"
db_path = base_path / db_name
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
    con = sqlite3.connect(base_path)
    cursor = con.cursor()
    housing_prices = cursor.execute("SELECT * FROM housing_prices").fetchall()
    con.close()

    return render_template("data_table.html", housing_prices=housing_prices)

if __name__=="__main__":
    app.run(debug=True)