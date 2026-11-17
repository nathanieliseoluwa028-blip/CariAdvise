# CariAdvise - Career Advice App

CariAdvise helps students find their best career match by answering 10 simple questions about their interests, favourite subjects, and how they like to work.

It shows your Top 2 career matches with score, why it fits you, and your first learning step.

Author: Nathaniel Isheoluwa

Live App: https://cariadvise.onrender.com

---

## PART 1: INSTALL WHAT YOU NEED

### 1. Install Python
1. Go to python.org/downloads
2. Download Python for Windows
3. During install, TICK "Add Python to PATH"
4. Click Install Now
5. Check it worked: Open Terminal and type:
   python --version

### 2. Install VS Code
1. Go to code.visualstudio.com
2. Download and Install VS Code
3. Open VS Code

### 3. Install Flask
Open Terminal in VS Code and type:
   pip install flask

---

## PART 2: CREATE THE PROJECT FOLDER

1. On your Desktop, create a new folder named: CariAdvise
2. In VS Code: File > Open Folder > Select CariAdvise
3. Inside CariAdvise, create these files and folders:

CariAdvise/
├── app.py
├── requirements.txt
├── Procfile
├── README.md
├── cariadvise.db (this is created automatically when you run the app)
└── templates/
    ├── index.html
    ├── quiz.html
    └── result.html

To create a file in VS Code: Right-click in the file list on left > New File > Type the name.

To create templates folder: Right-click > New Folder > Type templates. Then right-click templates > New File for each HTML file.

---

## PART 3: PUT THE CODE IN EACH FILE

### File 1: app.py
This is the main app.

In app.py:
1. Prepare your career list - Create a CAREERS dict with 5 careers. For each career, add a `why` (why it fits) and a `first_step` (first thing to learn).
2. Prepare your questions - Create a QUESTIONS list with 10 questions about interests, favourite subjects, and how you like to work.
3. Create routes - `/` for home, `/quiz` for quiz page, `/result` for result page.
4. Add scoring logic - Read answers from the quiz form, add points to each career, sort scores from highest to lowest, take Top 2.
5. Save result to database - Create cariadvise.db and save top career + score.
6. Pass data to result.html - Send `careers=CAREERS` and `scores=ranked` to the result page.

### File 2: templates/index.html
Home page with Welcome and Start Quiz button. It links to /quiz.

### File 3: templates/quiz.html
Shows the 10 questions. Each question has options. Form submits to /result.

### File 4: templates/result.html
Shows Top 2 careers with score, why, and first step. Use a loop to show the first 2 items from `scores`.

### File 5: requirements.txt
Tells Python what to install.Flask
gunicornjavascript
### File 6: Procfile
Tells Render how to start the app. No .txt, just named Procfile.web: gunicorn app:appjavascript
### File 7: README.md
This file you are reading now.

---

## PART 4: RUN IT ON YOUR COMPUTER

1. In VS Code Terminal, make sure you are inside CariAdvise folder:
   cd CariAdvise
2. Install requirements:
   pip install -r requirements.txt
3. Run the app:
   python app.py
4. Open browser and go to:
   http://127.0.0.1:5000
5. Click Start Quiz, answer 10 questions, see your Top 2 result.

---

## PART 5: PUSH TO GITHUB

1. Go to github.com > New Repository > Name: CariAdvise > Create
2. In VS Code Terminal:
   git init
   git add .
   git commit -m "First commit - CariAdvise app"
   git branch -M main
   git remote add origin https://github.com/YOUR-USERNAME/CariAdvise.git
   git push -u origin main
3. For every change after that:
   git add .
   git commit -m "Describe what you changed"
   git push
4. Refresh GitHub, you will see all files: app.py, templates, Procfile, requirements.txt, README.md, cariadvise.db

---

## PART 6: MAKE IT GO LIVE ON RENDER

1. Go to dashboard.render.com > Sign up with GitHub
2. Click New + > Web Service
3. Connect your CariAdvise repository
4. Settings:
   Name: cariadvise
   Build Command: pip install -r requirements.txt
   Start Command: gunicorn app:app
5. Click Create Web Service
6. Wait until Status says Live
7. Copy your live link, it looks like: https://cariadvise.onrender.com
8. Paste that link at the top of this README where it says Live App.
9. After any future change: Push to GitHub > Go to Render > Manual Deploy > Deploy latest commit.

---

## PROBLEMS WE FIXED

- Fixed Jinja2 UndefinedError by passing careers=CAREERS and scores=ranked to result.html
- Fixed double comma syntax error in render_template line in app.py
- Added why and first_step to each career in CAREERS dict
- Fixed result page to show Top 2, not just Top 1
