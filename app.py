from flask import Flask, render_template, request
import sqlite3, json

app = Flask(__name__, template_folder='templates')

CAREERS = {
    "Software Developer": {"desc": "You love building things with logic and code.", "first_step": "Learn Python basics on freeCodeCamp and build a calculator app.", "emoji": "💻"},
    "Data Analyst": {"desc": "You love finding patterns in numbers and facts.", "first_step": "Learn Excel + basic SQL, then make a chart from real data.", "emoji": "📊"},
    "Creative Designer": {"desc": "You love colours, stories and making things look beautiful.", "first_step": "Learn Canva/Figma and redesign your favourite app homepage.", "emoji": "🎨"},
    "Healthcare Professional": {"desc": "You love helping people and understanding how the body works.", "first_step": "Watch a first-aid course and volunteer at a school health drive.", "emoji": "🩺"},
    "Business & Entrepreneur": {"desc": "You love leading, selling ideas and starting things.", "first_step": "Write a 1-page business plan for an idea you have and pitch it to a friend.", "emoji": "🚀"}
}

QUESTIONS = [
    ("What do you enjoy most in free time?",
     [("Building games / apps", {"Software Developer": 3}),
      ("Looking at stats / sports data", {"Data Analyst": 3}),
      ("Drawing / editing videos", {"Creative Designer": 3}),
      ("Helping friends feel better", {"Healthcare Professional": 3}),
      ("Selling / planning a small business", {"Business & Entrepreneur": 3})]),
    ("Which school subject do you like best?",
     [("Maths / Computing", {"Software Developer": 2, "Data Analyst": 1}),
      ("Maths / Statistics", {"Data Analyst": 3}),
      ("Art / Music", {"Creative Designer": 3}),
      ("Biology / Chemistry", {"Healthcare Professional": 3}),
      ("Economics / Business Studies", {"Business & Entrepreneur": 3})]),
    ("How do you like to work?",
     [("Alone, solving puzzles", {"Software Developer": 2, "Data Analyst": 1}),
      ("With data and charts", {"Data Analyst": 3}),
      ("With colours and ideas", {"Creative Designer": 3}),
      ("With people, face to face", {"Healthcare Professional": 2, "Business & Entrepreneur": 1}),
      ("Leading a team", {"Business & Entrepreneur": 3})]),
    ("Pick a superpower:",
     [("Build anything with code", {"Software Developer": 3}),
      ("Predict the future from data", {"Data Analyst": 3}),
      ("Create anything you imagine", {"Creative Designer": 3}),
      ("Heal anyone instantly", {"Healthcare Professional": 3}),
      ("Turn any idea into money", {"Business & Entrepreneur": 3})]),
    ("What kind of problem excites you?",
     [("A bug in an app", {"Software Developer": 3}),
      ("Why sales went down", {"Data Analyst": 2, "Business & Entrepreneur": 1}),
      ("A boring poster that needs design", {"Creative Designer": 3}),
      ("Why someone is sick", {"Healthcare Professional": 3}),
      ("How to grow a shop", {"Business & Entrepreneur": 3})]),
    ("What would you do with N10,000?",
     [("Buy a coding course", {"Software Developer": 3}),
      ("Buy a data course / books", {"Data Analyst": 3}),
      ("Buy art supplies / camera", {"Creative Designer": 3}),
      ("Buy first-aid kit / science kit", {"Healthcare Professional": 3}),
      ("Start a small business", {"Business & Entrepreneur": 3})]),
    ("Which job sounds coolest?",
     [("App Developer", {"Software Developer": 3}),
      ("Data Scientist", {"Data Analyst": 3}),
      ("Graphic / UI Designer", {"Creative Designer": 3}),
      ("Doctor / Nurse", {"Healthcare Professional": 3}),
      ("CEO / Founder", {"Business & Entrepreneur": 3})]),
    ("How do you handle a hard task?",
     [("Break it into small code steps", {"Software Developer": 3}),
      ("Collect facts and compare", {"Data Analyst": 3}),
      ("Sketch many ideas first", {"Creative Designer": 3}),
      ("Stay calm and help others", {"Healthcare Professional": 3}),
      ("Make a plan and motivate people", {"Business & Entrepreneur": 3})]),
    ("What do friends ask you for help with?",
     [("Fixing phone / laptop", {"Software Developer": 2, "Data Analyst": 1}),
      ("Explaining numbers / homework", {"Data Analyst": 3}),
      ("Making posters / edits", {"Creative Designer": 3}),
      ("Advice when sad / hurt", {"Healthcare Professional": 3}),
      ("Organising events / money", {"Business & Entrepreneur": 3})]),
    ("Where do you want to work in future?",
     [("Tech company / from home", {"Software Developer": 2, "Data Analyst": 1}),
      ("Office with dashboards", {"Data Analyst": 3}),
      ("Studio / creative agency", {"Creative Designer": 3}),
      ("Hospital / clinic", {"Healthcare Professional": 3}),
      ("My own company", {"Business & Entrepreneur": 3})]),
]

def score_answers(answer_indexes):
    scores = {k: 0 for k in CAREERS}
    for q_idx, opt_idx in enumerate(answer_indexes):
        points = QUESTIONS[q_idx][1][opt_idx][1]
        for career, pts in points.items():
            scores[career] += pts
    return scores

def get_top_two(scores):
    # Tie handling: sort by -score, then name A-Z so ties are fair and always same
    ranked = sorted(scores.items(), key=lambda x: (-x[1], x[0]))
    return ranked[0], ranked[1], ranked

@app.route("/")
def index():
    return render_template("index.html", careers=CAREERS)

@app.route("/quiz", methods=["GET","POST"])
def quiz():
    if request.method == "POST":
        answers = []
        for i in range(len(QUESTIONS)):
            answers.append(int(request.form.get(f"q{i}", 0)))
        scores = score_answers(answers)
        top1, top2, ranked = get_top_two(scores)
        conn = sqlite3.connect("cariadvise.db")
        conn.execute("CREATE TABLE IF NOT EXISTS submissions (id INTEGER PRIMARY KEY AUTOINCREMENT, answers TEXT, result1 TEXT, result2 TEXT)")
        conn.execute("INSERT INTO submissions (answers, result1, result2) VALUES (?,?,?)", (json.dumps(answers), top1[0], top2[0]))
        conn.commit(); conn.close()
        return render_template("result.html", top1=top1, top2=top2, info2=CAREERS[top2[0]], scores=ranked)
    return render_template("quiz.html", questions=QUESTIONS)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)