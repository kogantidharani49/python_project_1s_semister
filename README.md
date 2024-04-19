# Housing Data Analysis Project
To write Python code to store the housing price data in a SQLite database and then serve that data up via a website . The dataset includes features such as price, area, bedrooms, bathrooms, and additional amenities.

## Prerequisites
Python 3.x

Flask

SQLite3

# Files
 **app.py** :   Contains the Flask application code.

 **Housing.db**: SQLite database with housing price data.

 **Housing_Price_Data.csv**: Raw housing price data.

 **Templates**: Directory for HTML templates.

 **index_links.html**: Home page template with links.

 **about.html**: About page template.

 **data_table.html**: Template for displaying data.


 ## References:
 https://www.kaggle.com/datasets/saurabhbadole/housing-price-data



# Goal of the Project:

**Database Setup**: It connects to a SQLite database named "Housing.db" and creates a table called "housing_prices" with columns for various attributes like price, area, bedrooms, etc.

**Data Population**: It reads data from a CSV file named "Housing_Price_Data.csv" and inserts it into the "housing_prices" table in the database. It skips the first row (header row) of the CSV file during insertion.

**Database Query**: It executes a SELECT query to fetch all the records from the "housing_prices" table.

**Flask Web Application**: It initializes a Flask web application. The application has three routes:
"/" route: Renders the "index_links.html" template. This template likely contains links to other pages or sections of the website.

"/about" route: Renders the "about.html" template. This template probably provides information about the project or the creators.

"/data" route: Connects to the SQLite database, retrieves the housing price data from the "housing_prices" table, and renders it using the "data_table.html" template.

The script demonstrates how to work with SQLite databases, CSV files, and Flask web applications for data visualization. It sets up a basic web interface to display housing price data stored in the SQLite database.
