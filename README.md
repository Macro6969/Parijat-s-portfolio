# Parijat Majumdar — Portfolio (Flask)

A single-page portfolio built with Python Flask, HTML (Jinja2), vanilla CSS and vanilla JavaScript.
No Node.js, npm or build step.

## Run it on Linux

```bash
# 1. Go into the project folder
cd parijat-portfolio

# 2. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Start the app
python app.py
```

Open **http://127.0.0.1:5000** in your browser. Stop the server with `Ctrl + C`.
Next time, just run `source venv/bin/activate` and `python app.py`.

> If `python3 -m venv` fails on Debian/Ubuntu: `sudo apt install python3-venv`.

## Where to change things

| What | Where |
|---|---|
| GitHub / LinkedIn / email | `CONTACT` in `app.py` (leave `None` to show "Not supplied") |
| Skills, pipeline steps, focus areas | `SKILLS`, `PIPELINE`, `FOCUS_AREAS` in `app.py` |
| Project text, hero copy, about text | `templates/index.html` |
| Colors, fonts, spacing | CSS variables at the top of `static/css/style.css` |
| Navigation visual (terrain, path) | `templates/partials/terrain_visual.html` |

Example, in `app.py`:

```python
CONTACT = {
    "github": "https://github.com/your-username",
    "linkedin": "https://www.linkedin.com/in/your-profile",
    "email": "you@example.com",
}
```

## Structure

```
parijat-portfolio/
├── app.py                      Flask app + editable content
├── requirements.txt
├── templates/
│   ├── base.html               header, footer, fonts
│   ├── index.html              all sections
│   ├── 404.html
│   └── partials/terrain_visual.html   reusable SVG visual
└── static/
    ├── css/style.css
    ├── js/script.js
    └── images/favicon.svg
```

## Notes

- Fonts (Space Grotesk, Inter, JetBrains Mono) load from Google Fonts; system fonts are used if offline.
- The telemetry numbers and visuals are labelled as simulated schematics, and the medical images are illustrative only.
- Animations are disabled automatically for visitors who prefer reduced motion.

## Deploying to parijatmajumdar.xyz

Don't use `debug=True` in production. Run with a production server, e.g.
`pip install gunicorn` then `gunicorn app:app`, behind Nginx or a host such as Render, Railway or PythonAnywhere.
