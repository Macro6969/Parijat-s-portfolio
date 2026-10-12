"""
Parijat Majumdar - Portfolio (Flask)

Run locally:
    python app.py
Then open http://127.0.0.1:5000

All the content you are most likely to edit (contact links, skills,
pipeline steps) lives in the dictionaries below. You do not need to touch
the HTML to change them.
"""

from datetime import date

from flask import Flask, render_template

app = Flask(__name__)

# ---------------------------------------------------------------------------
# SITE-WIDE SETTINGS
# ---------------------------------------------------------------------------
SITE = {
    "name": "Parijat Majumdar",
    "short_name": "Parijat",
    "domain": "parijatmajumdar.xyz",
    "github_repo": (
        "https://github.com/Macro6969/"
        "Anveshak---a-system-for-offroad-autonomous-ground-vehicle.git"
    ),
}

# ---------------------------------------------------------------------------
# CONTACT LINKS
# Leave a value as None while you do not have it: the site will then show it
# as "Not supplied" instead of a broken link.
# Examples once you are ready:
#   "github":   "https://github.com/your-username"
#   "linkedin": "https://www.linkedin.com/in/your-profile"
#   "email":    "you@example.com"
# ---------------------------------------------------------------------------
CONTACT = {
    "github": None,
    "linkedin": None,
    "email": None,
}

# ---------------------------------------------------------------------------
# FOCUS AREAS (strip under the hero)
# ---------------------------------------------------------------------------
FOCUS_AREAS = [
    "AI / ML",
    "Computer Vision",
    "Autonomous Robotics",
    "Software Development",
]

# ---------------------------------------------------------------------------
# ENGINEERING PIPELINE
# "icon" must match one of the names handled in templates/index.html
# ---------------------------------------------------------------------------
PIPELINE = [
    {
        "name": "PERCEIVE",
        "icon": "eye",
        "text": "Interpret the scene. Separate traversable terrain from the "
                "surrounding environment.",
        "tags": "Camera + Semantic segmentation",
    },
    {
        "name": "LOCALIZE",
        "icon": "crosshair",
        "text": "Estimate motion from visual cues. Build an understanding of "
                "the vehicle's pose.",
        "tags": "Features + Visual odometry",
    },
    {
        "name": "MAP",
        "icon": "map",
        "text": "Connect observations into a spatial model of the world "
                "around the vehicle.",
        "tags": "Observations + World model",
    },
    {
        "name": "NAVIGATE",
        "icon": "route",
        "text": "Plan a route through the mapped terrain. Turn perception "
                "into directed movement.",
        "tags": "World model + Path planning",
    },
]

# ---------------------------------------------------------------------------
# SKILLS
# ---------------------------------------------------------------------------
SKILLS = [
    {
        "title": "Programming",
        "icon": "code",
        "items": ["Python", "C", "Kotlin"],
    },
    {
        "title": "AI & Computer Vision",
        "icon": "eye",
        "items": ["Machine Learning", "OpenCV", "Semantic Segmentation",
                  "Image Processing"],
    },
    {
        "title": "Robotics & Algorithms",
        "icon": "route",
        "items": ["Visual Odometry", "Path Planning", "A* Search",
                  "Autonomous Navigation"],
    },
    {
        "title": "Development",
        "icon": "git",
        "items": ["Git", "GitHub", "Android Development"],
    },
]


@app.route("/")
def index():
    """Home page: the whole portfolio is a single scrolling page."""
    return render_template(
        "index.html",
        site=SITE,
        contact=CONTACT,
        focus_areas=FOCUS_AREAS,
        pipeline=PIPELINE,
        skills=SKILLS,
        year=date.today().year,
    )


@app.errorhandler(404)
def not_found(_error):
    """Friendly page for unknown URLs."""
    return render_template("404.html", site=SITE, year=date.today().year), 404


if __name__ == "__main__":
    # debug=True reloads the server when you edit files. Turn it off in production.
    app.run(host="127.0.0.1", port=5000, debug=True)
