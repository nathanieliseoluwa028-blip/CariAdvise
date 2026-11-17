# CariAdvise - Career Advice App

CariAdvise helps students find their best career match by answering 10 simple questions about their interests, favourite subjects, and how they like to work.

## Features
- 10-question career quiz
- 5 careers: Software Developer, Data Analyst, Creative Designer, Healthcare Professional, Business & Entrepreneur
- Shows Top 2 matches with score, reason (Why this fits you) and first learning step
- Saves every result to SQLite database (cariadvise.db)

## How to Run Locally
1. Install Python
2. Install Flask: `pip install flask`
3. Run: `python app.py`
4. Open browser: `http://127.0.0.1:5000`

## How to Deploy on Render
- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn app:app`
- Procfile included

## Support / Problems Fixed
- Fixed Jinja2 UndefinedError by passing `careers=CAREERS` and `scores=ranked` to result.html
- Fixed double comma syntax error in render_template line
- Added `why` and `first_step` to each career in CAREERS dict

## Author
Nathaniel Isheoluwa