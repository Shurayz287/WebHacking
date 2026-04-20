from flask import Flask, request

app = Flask(__name__)

FLAG = "shurayz287{1P_Sp00f1ng}"
request_conter = 0
requests_ip = []
@app.route("/")
def home():
    global request_conter, requests_ip
    hostheader = request.headers.get("X-Forwarded-For", "127.0.0.1")
    if hostheader not in requests_ip: 
        requests_ip.append(hostheader)
        request_conter += 1
        if request_conter >= 2: return FLAG
        return "This is the first time!"
    else:
        return "Only request once time!"
    return ""
    

app.run(host="0.0.0.0", port=28071)
