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
    "resume_url": None,
}

ABOUT = (
    "I'm a third-year AI & DS student focused on building practical, "
    "readable, and user-friendly projects. I enjoy turning ideas into working demos "
    "and I'm open to internships."
)

EDUCATION = [
    {
        "title": "B.Tech — Artificial Intelligence & Data Science",
        "org": "SNS College of Engineering, Coimbatore",
        "period": "2023 — Present"
    }
]

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
                "desc": "A Flutter-based web app that connects blood donors and recipients with smart eligibility checks and easy donation management.",
                "code_url": "https://github.com/Keshi-646/blood-bank"
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
                "desc": "Developed a system to classify emails as spam or legitimate using Python and machine learning.",
                "code_url": "https://github.com/Keshi-646/Spam-Email-Detection"
            }
        ]
    }, 

    {
        "company": "Skypark iTech",
        "period": "January 2026",
        "role": "Intern",
        "bullets": [
            "I gained experience in Web developer."
        ],
        "projects": [
            {
                "title": "E-Sevai App",
                "desc": "Developed a e-sevai web app for client.",
                "code_url": "https://github.com/Keshi-646/esevai"
            }
        ]
    }
]


PROJECTS = [
    {
        "title": "HireFusion",
        "desc": "An AI-powered recruitment and hiring platform engineered to streamline candidate evaluation, automate resume analysis, and optimize hiring workflows through intelligent automation and smart decision-making support — transforming how organizations discover and onboard top talent.",
        "tags": ["AI", "Recruitment", "Automation", "Python"],
        "links": [
            {"label": "Code", "url": "https://github.com/Keshi-646/hirefusion-"},
        ],
        "image": "project5.png",
        "featured": True,
    },
    {
        "title": "Blood Bank App",
        "desc": "A robust Flutter-based platform engineered to seamlessly connect blood donors with recipients in need. Features intelligent eligibility validation, real-time donor matching, and streamlined donation management — making life-saving connections faster and more reliable.",
        "tags": ["Flutter", "Dart"],
        "links": [
            {"label": "Code", "url": "https://github.com/Keshi-646/blood-bank"},
        ],
        "image": "project4.png",
        "featured": False,
    },
    {
        "title": "Spam Email Detection",
        "desc": "A high-accuracy machine learning system built with Python to intelligently classify incoming emails as spam or legitimate. Leverages advanced text processing and classification algorithms to protect users from unwanted and malicious email content.",
        "tags": ["Python", "Machine Learning", "NLP"],
        "links": [
            {"label": "Code", "url": "https://github.com/Keshi-646/Spam-Email-Detection"},
        ],
        "image": "project1.png",
        "featured": False,
    },
    {
        "title": "Speech Therapy App",
        "desc": "An innovative Python-based application delivering personalized speech therapy exercises with real-time feedback and comprehensive progress tracking. Designed to make professional-grade speech therapy more accessible, engaging, and effective for users of all ages.",
        "tags": ["Python"],
        "links": [
            {"label": "Code", "url": "https://github.com/Keshi-646/Speech-Therapy"},
        ],
        "image": "project2.png",
        "featured": False,
    },
    {
        "title": "Enunciating Dictionary",
        "desc": "A feature-rich offline dictionary application built with Python Tkinter and JSON, delivering instant word meanings, definitions, and pronunciation guides — all without requiring an internet connection.",
        "tags": ["Python", "Tkinter", "JSON"],
        "links": [
            {"label": "Code", "url": "https://github.com/Keshi-646/Enunciating-Dict"},
        ],
        "image": "project3.png",
        "featured": False,
    },
]

ACHIEVEMENTS = [
    {
        "title": "Paper Presentation on Agriculture",
        "when": "2023",
        "summary": "Banari Amman Institute of Technology",
        "url": "https://drive.google.com/file/d/1wkUGiiILVI5QNhCuaqB989El6D4iRAcA/view?usp=sharing",
        "icon": "🏆",
    },
    {
        "title": "Math Quiz",
        "when": "2024",
        "summary": "KGiSL Institute of Technology",
        "url": "https://drive.google.com/file/d/1noKH24lpDR39dUUFVIIbbGLJYRbj4zD1/view?usp=drive_link",
        "icon": "🧮",
    },
    {
        "title": "UI & UX Unplugged",
        "when": "2025",
        "summary": "Karpagam Institute of Technology",
        "url": "https://drive.google.com/file/d/1RD5hfdgw6_fbbqZ7iAuyPF4J9A3Or6BV/view?usp=drive_link",
        "icon": "🎨",
    },
    {
        "title": "Data Quest",
        "when": "2025",
        "summary": "Karpagam Institute of Technology",
        "url": "https://drive.google.com/file/d/1svAKCOdgebbzI3KXwJoS32EKewLAxQyQ/view?usp=drive_link",
        "icon": "📊",
    },
]

SKILLS = [
    {"name": "Python", "icon": "🐍", "category": "Languages"},
    {"name": "MySQL", "icon": "🗄️", "category": "Database"},
    {"name": "Flutter", "icon": "📱", "category": "Frameworks"},
    {"name": "Streamlit", "icon": "⚡", "category": "Frameworks"},
    {"name": "GenAI", "icon": "🤖", "category": "AI/ML"},
    {"name": "Agentic AI", "icon": "🧠", "category": "AI/ML"},
    {"name": "HTML/CSS", "icon": "🌐", "category": "Web"},
    {"name": "n8n", "icon": "🔄", "category": "Automation"},
]

# ----------------------------- ROUTES -----------------------------
@app.route("/", methods=["GET"])
def home():
    profile_img = (
        url_for("static", filename="profile.jpeg")
        if static_exists("profile.jpeg")
        else "https://via.placeholder.com/240x240.png?text=Your+Photo"
    )
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

    with open(os.path.join(BASE_DIR, "messages.txt"), "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now().isoformat(sep=' ', timespec='seconds')}] {name} <{email}>: {message}\n")

    flash("Thank you! Your message has been sent successfully. I'll get back to you soon!", "success")
    return redirect(url_for("home") + "#contact")

# ----------------------------- MAIN -----------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
