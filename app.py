from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Pages that can be searched
PAGES = {
    "home": {"title": "Home", "url": "/"},
    "projects": {"title": "Projects", "url": "/projects"},
    "project1": {"title": "This Website", "url": "/project1"},
    "project2": {"title": "Cipherforge", "url": "/project2"},
    "contact": {"title": "Contact", "url": "/contact"},
}


@app.route("/")
def home():
    return render_template("index.html")


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
