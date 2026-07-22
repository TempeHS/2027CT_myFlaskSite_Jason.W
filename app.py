import random
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


PAGES = {
    "home": {"title": "Home", "url": "/"},
    "projects": {"title": "Projects", "url": "/projects"},
    "project1": {"title": "This Website", "url": "/project1"},
    "project2": {"title": "Cipherforge", "url": "/project2"},
    "contact": {"title": "Contact", "url": "/contact"},
}


QUOTES = [
    "The only way to do great work is to love what you do. – Steve Jobs",
    "In the middle of every difficulty lies opportunity. – Albert Einstein",
    "It does not matter how slowly you go as long as you do not stop. – Confucius",
    "Life is what happens when you're busy making other plans. – John Lennon",
    "The future belongs to those who believe in the beauty of their dreams. – Eleanor Roosevelt",
    "Success is not final, failure is not fatal: it is the courage to continue that counts. – Winston Churchill",
    "You only live once, but if you do it right, once is enough. – Mae West",
    "In three words I can sum up everything I've learned about life: it goes on. – Robert Frost",
]


@app.route("/")
def home():
    quote = random.choice(QUOTES)
    return render_template("index.html", quote=quote)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/projects")
def projects():
    return render_template("projects.html")


@app.route("/project1")
def project1():
    return render_template("project1.html")


@app.route("/project2")
def project2():
    return render_template("project2.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/search")
def search():
    query = request.args.get("q", "").strip().lower()
    for key, page in PAGES.items():
        if query in page["title"].lower() or query in key.lower():
            return redirect(page["url"])
    return render_template("search_404.html", query=query)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


@app.route("/about")
def about():
    return render_template("about.html")
