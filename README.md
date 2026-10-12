# Parijat Majumdar — Portfolio

A responsive personal portfolio built with Python, Flask, Jinja2, CSS, and JavaScript. It features ANVESHAK, the Recursive Hackathon 2026 first-place result, a conceptual overview of the navigation pipeline, and project cards for other experiments. The visual diagrams are illustrative, not measured system output.

## Run locally

Python 3.10 or newer is recommended.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000. Check the health endpoint at http://127.0.0.1:5000/health.

## Update links and add projects

Open `app.py`. At the top, edit the `PROFILE` dictionary:

```python
PROFILE = {
    "name": "Parijat Majumdar",
    "domain": "parijatmajumdar.xyz",
    "github": "https://github.com/Macro6969",
    "linkedin": "https://www.linkedin.com/in/your-profile/",
    "email": "you@example.com",
}
```

To hide LinkedIn or email until you are ready, set that value to an empty string (`""`).

To add a project, add another dictionary to the `PROJECTS` list in `app.py`:

```python
{
    "name": "Project name",
    "category": "AI / COMPUTER VISION",
    "description": "A concise, accurate description of what the project does.",
    "technologies": ["Python", "OpenCV"],
    "url": "https://github.com/your-username/your-repository",
},
```

Use the exact repository URL and only claim features you have implemented. The website generates a project card for every entry in `PROJECTS`; no HTML changes are needed for ordinary project additions. ANVESHAK remains the featured project.

## Production deployment

Use a production WSGI server rather than Flask's local development server. For a Linux host that supports Python processes, install the requirements and run:

```bash
gunicorn --workers 2 --bind 0.0.0.0:${PORT:-8000} app:app
```

Configure the hosting platform to forward public HTTPS traffic to the app process and set `PORT`, `FLASK_SECRET_KEY`, and any contact variables in its environment settings. Point `parijatmajumdar.xyz` and `www.parijatmajumdar.xyz` to the host using the DNS records provided by your hosting provider, then enable HTTPS there.

The profile links and project list are configured at the top of `app.py`. Update those values when your links or projects change. Keep descriptions aligned with the current implementation, and avoid presenting illustrative diagrams as real-time outputs or measured results. The ANVESHAK pipeline section is a conceptual overview; it does not claim that every component is production-ready or validated.


## Adding a project image

1. Put the image or SVG in `static/images/` (for example `static/images/my-project.svg`).
2. Add `"image": "images/my-project.svg"` and an optional `"image_alt": "A short description"` to that project's dictionary in `PROJECTS` in `app.py`.
3. Save and run the site. The template renders the image automatically. For deployment, commit and push the new image file along with the code.

Use screenshots or diagrams that represent the actual implementation when possible. The included Agnirakshak and FloodGuard SVGs are clearly schematic concept illustrations, not real model outputs or evidence of project results.
