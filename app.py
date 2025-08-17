"""
CS50 Final Project — Show Search App (Backend)
Author: Rashad Yusufzai (RY-IT / RashYus1)
City, Country: Gothenburg, Sweden
Date: 2025-08-13

Description:
    This is the backend for the Show Search App, built using Flask and SQLite.
    It serves HTML templates, responds to AJAX requests with JSON data, and
    provides two main routes: /popular and /search for retrieving show info.

Technologies used:
    - Python 3
    - Flask (lightweight web framework)
    - SQLite (local database)
    - CS50's SQL library (simplifies database interaction)
    - Jinja2 (template rendering)

Note:
Some documentation and formatting guidance were assisted by AI tools.
All core logic, database setup, and functionality were implemented manually.

Port Info:
    When running locally, open http://127.0.0.1:5000 in your browser to view the app.
"""

from cs50 import SQL  # type: ignore # SQLite interface
from flask import Flask, jsonify, render_template, request # type: ignore

# Initialize Flask app
app = Flask(__name__)

# Connect to SQLite database (local file)
db = SQL("sqlite:///shows.db")

# Route: Home page
@app.route("/")
def index():
    """Render the homepage."""
    return render_template("index.html")

# Route: Search shows
@app.route("/search")
def search():
    """Search shows by title."""
    q = request.args.get("q")
    if q:
        # If no query is provided, return popular shows
        results = db.execute(
            """
            SELECT title, genre, year, rating, description, image_url 
            FROM shows 
            WHERE title LIKE ? 
            LIMIT 50
            """,
            f"%{q}%"
        )

        # If no results found, return a default “no results” card
        if not results:
            results = [{
                "title": "No results found",
                "genre": "N/A",
                "year": "N/A",
                "rating": 0,
                "description": "",
                "image_url": "/static/images/broken_image.png"  # No image for default card
            }]
    else:
        # If empty query, return first 4 popular shows
        results = db.execute(
            """
            SELECT title, genre, year, rating, description, image_url 
            FROM shows 
            LIMIT 4
            """
        )
    return jsonify(results)

# Route: Popular shows
@app.route("/popular")
def popular():
    """Return first 4 shows as popular on homepage load."""
    results = db.execute(
        """
        SELECT title, genre, year, rating, description, image_url 
        FROM shows 
        LIMIT 4
        """
    )
    return jsonify(results)

# Start the Flask development server
if __name__ == "__main__":
    app.run(debug=True)
