import os

checks = [
    ("frontend dir", os.path.isdir("frontend")),
    ("style.css", os.path.exists("frontend/style.css")),
    ("index.html", os.path.exists("frontend/index.html") or os.path.exists("index.html")),
    ("requirements.txt", os.path.exists("requirements.txt"))
]

for name, ok in checks:
    print(f"{name:20} : {'OK' if ok else 'MISSING'}")
