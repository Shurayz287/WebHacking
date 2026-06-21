from flask import Flask, request, redirect, url_for, render_template_string

app = Flask(__name__)
comments = []
msg = ""

HTML = """
<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <title>Stored XSS Lab</title>
</head>
<body>
    <h2>Stored XSS Lab</h2>

    <form method="POST">
        <input name="comment" placeholder="Nhập bình luận..." style="width:300px;">
        <button type="submit">Gửi</button>
    </form>

    <p><a href="/reset">Reset data</a></p>

    <h3>Bình luận</h3>
    <ul>
        {% for c in comments %}
            <li>{{ c|safe }}</li>
        {% endfor %}
    </ul>
    <h2> Reflected XSS </h2>
    <h3>{{ msg|safe }}</h3>

    <h3>{{ q|safe }}</h3> 
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    global msg
    if request.method == "POST":
        comment = request.form.get("comment", "")
        comments.append(comment)
        msg = f"Added {comment} successfull"
        return redirect(url_for("index"))
    query = request.args.get("q", "")
    return render_template_string(HTML, comments=comments, msg=msg, q=query)

@app.route("/reset")
def reset():
    global msg
    comments.clear()
    msg = ""
    return redirect(url_for("index"))

app.run()