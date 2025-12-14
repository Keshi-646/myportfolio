from flask import Flask, render_template, request, redirect, url_for, flash
import os
from datetime import datetime

app = Flask(__name__)
app.config["SECRET_KEY"] = "change-this-in-production"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def static_exists(fname: str) -> bool:
    return os.path.exists(os.path.join(BASE_DIR, "static", fname))

# ----------------------------- CONTENT -----------------------------
PROFILE = {
    "name": "Keshiya V",
    "tagline": "Aspiring AI Engineer",
    "location": "Theni, India",
    "email": "keshipraba95228@gmail.com",
    "github": "https://github.com/Keshi-646",
    "linkedin": "https://www.linkedin.com/in/keshiya-v",
    "resume_url": None,  # e.g. url_for('static', filename='resume.pdf') after you add it
}

ABOUT = (
    "I’m a third-year AI & DS student focused on building practical, "
    "readable, and user-friendly projects. I enjoy turning ideas into working demos "
    "and I’m open to internships."
)

EDUCATION = [
    {
        "title": "B.Tech — Artificial Intelligence & Data Science",
        "org": "SNS College of Engineering, Coimbatore",
        "period": "2023 — Present"
    }
]

# ------------------- EXPERIENCE (grouped by company) -------------------
EXPERIENCE = [
    {
        "company": "Kevell Global Solutions",
        "period": "August 2024",
        "role": "Intern",
        "bullets": [
            "I gained experience in Flutter development."
        ],
        "projects": [
            {
                "title": "Blood Bank App",
                "period": "2025",
                "desc": "Browser-based scanner; integrated LLM for parsing.",
                "code_url": "https://github.com/Keshi-646/BarcodeScanner"   # <--- ADD THIS
            }
        ]
    },

    {
        "company": "Ascentz Technologies",
        "period": "June 2025",
        "role": "Intern",
        "bullets": [
            "Focused on Machine Learning concepts and applications."
        ],
        "projects": [
            {
                "title": "Spam Email Detection",
                "period": "2025",
                "desc": "Developed a system to classify emails as spam or legitimate using Python and machine learning.",
                "code_url": "https://github.com/Keshi-646/Spam-Email-Detection"        # <--- ADD THIS
            }
        ]
    }
]


PROJECTS = [
    {
        "title": "Spam Email Detection",
        "desc": "Developed a system to classify emails as spam or legitimate using Python and machine learning. ",
        "tags": ["Python", "ML"],
        "links": [
            #{"label": "Live", "url": "#"},
            {"label": "Code", "url": "https://github.com/Keshi-646/Spam-Email-Detection"},
        ],
        "image": "project1.png",  # put this in /static if you have it
    },
    {
        "title": "Speech Therapy",
        "desc": "Designed and developed a Speech Therapy App providing personalized exercises, real-time feedback, and progress tracking. - Aimed at making speech therapy more engaging, effective, and widely available.",
        "tags": ["Python"],
        "links": [
            #{"label": "Demo", "url": "#"},
            {"label": "Code", "url": "https://github.com/Keshi-646/Speech-Therapy"},
        ],
        "image": "project2.png",
    },
    {
        "title": "Enunciating Dictionary",
        "desc": "Built an offline app using Tkinter and JSON for word meanings and pronunciation",
        "tags": ["Python", "JSON"],
        "links": [
            #{"label": "Live", "url": "#"},
            {"label": "Code", "url": "https://github.com/Keshi-646/Enunciating-Dict"},
        ],
        "image": "project3.png",
    },
]

ACHIEVEMENTS = [
    {
        "title": "Paper presentation on Agriculture",
        "when": "2023",
        "summary": "Banari Amman Institute of Technology",
        "url": "https://drive.google.com/file/d/1wkUGiiILVI5QNhCuaqB989El6D4iRAcA/view?usp=sharing",
    },
    {
        "title": "Math Quiz",
        "when": "2024",
        "summary": "KGiSL Institute of Technology",
        "url": "https://drive.google.com/file/d/1noKH24lpDR39dUUFVIIbbGLJYRbj4zD1/view?usp=drive_link",
    },
    {
        "title": "UI&UX Unplugged",
        "when": "2025",
        "summary": "Karpagam Institute of Technology",
        "url": "https://drive.google.com/file/d/1RD5hfdgw6_fbbqZ7iAuyPF4J9A3Or6BV/view?usp=drive_link",
    },
    {
        "title": "Data Quest",
        "when": "2025",
        "summary": "Karpagam Institute of Technology",
        "url": "https://drive.google.com/file/d/1svAKCOdgebbzI3KXwJoS32EKewLAxQyQ/view?usp=drive_link",
    },
]

SKILLS = [
    "Python", "MySQL", "Flutter", "Streamlit", "GenAI",
    "Agentic AI", "HTML/CSS basics", "n8n"
]

# ----------------------------- ROUTES -----------------------------
@app.route("/", methods=["GET"])
def home():
    profile_img = (
        url_for("static", filename="profile.jpeg")
        if static_exists("profile.jpeg")
        else "https://via.placeholder.com/240x240.png?text=Your+Photo"
    )
    # Optional resume
    resume_url = PROFILE["resume_url"]
    if resume_url is None and static_exists("resume.pdf"):
        resume_url = url_for("static", filename="resume.pdf")

    return render_template(
        "index.html",
        now_year=datetime.now().year,
        profile=PROFILE,
        about=ABOUT,
        education=EDUCATION,
        experience=EXPERIENCE,
        projects=PROJECTS,
        writing=ACHIEVEMENTS,
        skills=SKILLS,
        profile_img=profile_img,
        resume_url=resume_url,
    )

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()

    if not name or not email or not message:
        flash("Please fill in all contact fields.", "danger")
        return redirect(url_for("home"))

    # Minimal “store” — append to a text file (replace with email service in prod)
    with open(os.path.join(BASE_DIR, "messages.txt"), "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now().isoformat(sep=' ', timespec='seconds')}] {name} <{email}>: {message}\n")

    flash("Thanks! Your message was sent successfully.", "success")
    return redirect(url_for("home"))

# ----------------------------- MAIN -----------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

