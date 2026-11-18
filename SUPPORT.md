# CariAdvise - Support Report

Author: Nathaniel Isheoluwa
Project: CariAdvise - Career Advice App
Live App: https://cariadvise.onrender.com

## What This Report Covers
This report lists the problems I had while building CariAdvise, how I fixed them, and how the app is supported.

## Problems I Fixed

### 1. Jinja2 UndefinedError - careers / scores not defined
Problem: Result page showed error "careers is undefined" and "scores is undefined".
Cause: In app.py, I did not pass the data to result.html.
Fix: Changed the return line to:
return render_template("result.html", careers=CAREERS, scores=ranked)
Result: Result page now loads correctly.

### 2. Double Comma Syntax Error in app.py
Problem: App would not start, Python showed syntax error.
Cause: I had a double comma ,, in the render_template line.
Fix: Removed the extra comma and checked the whole file.
Result: App started working.

### 3. Result Page Showed Only Top 1 Instead of Top 2
Problem: Task requires Top 2 career matches, but only 1 was showing.
Cause: Template was only showing the first item.
Fix: Used a loop to show the first 2 items from scores.
Result: Result page now shows Top 2 with reason and first step.

### 4. Missing why and first_step For Each Career
Problem: Result page could not show why a career fits or what to learn first.
Cause: CAREERS dict only had names, no details.
Fix: Added why and first_step to every career in CAREERS dict.
Result: Each result now shows reason + first learning step.

### 5. Render Deployment - App Not Starting
Problem: Render showed build error / app not live.
Cause: Missing Procfile and requirements.txt, or wrong Start Command.
Fix: Added Procfile with `web: gunicorn app:app` and requirements.txt with Flask + gunicorn.
Set Build Command to `pip install -r requirements.txt` and Start Command to `gunicorn app:app`.
Result: App deployed successfully and is live.

## How Scoring and Ties Are Handled
See README.md section "HOW SCORING WORKS" and "HOW TIED SCORES ARE HANDLED" for full explanation.

## How To Get Support / Report A Problem
1. Check README.md - Setup Guide for install, run, GitHub, and Render steps.
2. Check this Support Report for known problems.
3. If the app is slow on first load, wait 30-50 seconds - Render free plan sleeps when not used.
4. If you find a new bug, open an Issue on GitHub with: what you clicked, what you expected, what error you saw, and a screenshot.

## Files In This Project
app.py - Main app, quiz logic, scoring
templates/index.html - Home page
templates/quiz.html - Quiz page
templates/result.html - Result page
requirements.txt - Flask + gunicorn
Procfile - Tells Render how to start app
cariadvise.db - Database that saves results
README.md - Setup guide
SUPPORT.md - This support report
