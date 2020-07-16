from flask import Flask, send_file, request, send_from_directory, render_template, redirect
from operations import combineWifi, connetWIFI
import time
app = Flask(__name__)

@app.route("/")
def index():
    fl = combineWifi()
    return render_template("index.html", data=fl)

@app.route("/connect/<ssid>", methods=["GET", "POST"])
def input(ssid):
    if request.method == "POST":
        data = request.form.to_dict()
        ssid = data["ssid"]
        password = data["password"] 
        print(ssid, password)
        connetWIFI(ssid, password)
        time.sleep(5)
        return redirect("/")
    else:
        return render_template("connect.html", SSID=ssid)

time.sleep(50)
app.run(host="0.0.0.0", port=8888, threaded=True, debug=True)