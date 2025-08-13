# Final Project - CS50

CS50 Final Project – Show search app built with Python, SQLite, SQL, HTML, Jinja2, CSS, JavaScript, Ajax (Fetch API), JSON, and Flask-Session.

This project is a Flask web app that lets users search for TV shows.

## Project Overview

This Flask web app lets users search for TV shows by title. It stores data in a local SQLite database (`shows.db`) and returns results as JSON from a `/search?q=` endpoint. The homepage uses JavaScript (Fetch API) to call that endpoint and update the list instantly without a full page reload. The project demonstrates:

- Python + Flask for routing and server logic
- SQLite + SQL for data storage and queries
- HTML + Jinja2 for templates
- JavaScript (Fetch API) for AJAX

## Features

- Search shows by title using AJAX
- Shows results dynamically on the homepage

## Setup Instructions

1. **Clone the repository**
   bash
   git clone [https://github.com/RashYus1/final_project.git](https://github.com/RashYus1/final_project.git)
   cd final_project

## How to run

1. Install dependencies: `pip install -r requirements.txt`
2. Run the app: `python3 app.py`
3. Open your browser and go to `http://localhost:5000`

## AI Disclosure

This project was developed by Rashad Yusufzai with assistance from AI tools.
