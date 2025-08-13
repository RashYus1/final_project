# Final Project - CS50

CS50 Final Project – Show search app built with Python, SQLite, SQL, HTML, Jinja2, CSS, JavaScript, and Flask.

This project is a Flask web app that lets users search for TV shows.

## Project Overview

This Flask web app allows users to search for TV shows by title. It stores data in a local SQLite database (`shows.db`) and returns results as JSON from the `/search?q=` endpoint. The homepage uses JavaScript (Fetch API) to update the list dynamically without reloading the page.  

The project demonstrates:

- Python + Flask for server logic and routing  
- SQLite + SQL for database queries  
- HTML + Jinja2 for templates  
- JavaScript (Fetch API) for AJAX

## Features

- Search shows by title using AJAX  
- Display results dynamically on the homepage

## Setup Instructions

1. **Clone the repository**

    ```bash
   git clone https://github.com/RashYus1/final_project.git
   cd final_project

## Folder Structure

final_project/
│
├── app.py                 # Main Flask app
├── requirements.txt       # Python dependencies
├── shows.db               # SQLite database with TV show data
├── README.md              # Project documentation
│
├── templates/             # HTML templates (Jinja2)
│   ├── layout.html
│   ├── index.html
│   └── search.html
│
├── static/                # Static files (images, CSS, JS)
│
└── froshims/              # Additional Flask app from CS50 problem set
    ├── app.py
    ├── templates/
    └── static/

## How to run

1. Install dependencies: `pip install -r requirements.txt`
2. Run the app: `python3 app.py`
3. Open your browser and go to `http://localhost:5000`

## AI Disclosure

This project was developed by Rashad Yusufzai with assistance from AI tools.
