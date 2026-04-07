from flask import Flask, request

app = Flask(__name__)

FLAG = "shurayz287{y0u_kn0w}"

@app.route("/")
def home():
    hostheader = request.headers.get("Host")
    if hostheader == "127.0.0.1": 
        return FLAG
    return "Welcome to my web page"

app.run(host="0.0.0.0", port=36363)
