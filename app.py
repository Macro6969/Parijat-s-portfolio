from flask import Flask, render_template

app = Flask(__name__)

# Edit this dictionary to update public profile/contact links.
# Leave a value as an empty string to hide that link on the website.
PROFILE = {
    "name": "Parijat Majumdar",
    "domain": "parijatmajumdar.xyz",
    "github": "https://github.com/Macro6969",
    "linkedin": "https://www.linkedin.com/in/parijat-majumdar-020b0a267/",  # Example: https://www.linkedin.com/in/your-profile/
    "email": "masterparijat@gmail.com",     # Example: you@example.com
}

# Add or remove projects here. Each project appears in the additional projects section.
# Keep descriptions accurate to what you have actually implemented.
PROJECTS = [
    {
        "name": "Agnirakshak",
        "category": "AI / ENVIRONMENTAL INTELLIGENCE",
        "description": "A project exploring wildfire prediction and threat analysis. See the repository for implementation details.",
        "technologies": ["Python", "Machine Learning"],
        "url": "https://github.com/Macro6969/Agnirakshak",
        "image": "images/agnirakshak.svg",
        "image_alt": "Schematic wildfire observation map with perimeter and sensor points",
    },
    {
        "name": "FloodGuard",
        "category": "AI / FLOOD RISK",
        "description": "A project focused on flood-related risk analysis. See the repository for its current features and implementation.",
        "technologies": ["Python"],
        "url": "https://github.com/Macro6969/FloodGuard",
        "image": "images/floodguard.svg",
        "image_alt": "Schematic flood monitoring map with river channel and observation markers",
    },
]

ANVESHAK_URL = "https://github.com/Macro6969/Anveshak---a-system-for-offroad-autonomous-ground-vehicle.git"

@app.get("/")
def home():
    return render_template(
        "index.html",
        profile=PROFILE,
        projects=PROJECTS,
        project_url=ANVESHAK_URL,
    )

@app.get("/health")
def health():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(__import__("os").environ.get("PORT", "5000")), debug=False)
