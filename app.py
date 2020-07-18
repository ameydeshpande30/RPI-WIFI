from flask import Flask, send_file, request, send_from_directory, render_template, redirect
from operations import combineWifi, connetWIFI
from db import addNetwrok, getAllNetwork, getPassword, changePassword
import time, json
app = Flask(__name__)
path = "./"
data = open(path + "config.json",'r').read()
val = json.loads(data)
WAKE_TIME = val["WAKE_TIME"]   # Time For System Network to boot up
CONNECT_TIME = val["CONNECT_TIME"] # time for system to change wifi

@app.route("/")
def index():
    fl = combineWifi()
    ll = []
    for i in fl:
        if str(i["ssid"]).strip() == "":
            pass
        else:
            val, passs = getPassword(i["ssid"])
            print(val)
            if val == 1:
                newi = {}
                newi["ssid"] = i["ssid"]
                newi["code"] = 1
                newi["del"] = 1
                ll.append(newi)
                continue
            ll.append(i)
    # print(ll)
    return render_template("index.html", data=ll)

@app.route("/delete/<ssid>")
def changePassword(ssid):
    return render_template("connect.html", SSID=ssid)

@app.route("/connect/<ssid>", methods=["GET", "POST"])
def input(ssid):
    if request.method == "POST":
        data = request.form.to_dict()
        ssid = data["ssid"]
        check, passs = getPassword(ssid=ssid)
        password = data["password"] 
        if check == 1 :
            changePassword(ssid, password)
        else:
            addNetwrok(ssid, password)
        # print(ssid, password)
        connetWIFI(ssid, password, 0)
        time.sleep(CONNECT_TIME)
        return redirect("/")
    else:
        check, passs = getPassword(ssid=ssid)
        if check == 1:
            connetWIFI(ssid, passs, 0)
            time.sleep(CONNECT_TIME)
            return redirect("/")
        return render_template("connect.html", SSID=ssid)

def startData():
    ll = getAllNetwork()
    z = 1
    for i in ll:
        connetWIFI(i["ssid"], i["password"], z)
        z = z + 1

time.sleep(WAKE_TIME)
app.run(host="0.0.0.0", port=8888, threaded=True, debug=False)