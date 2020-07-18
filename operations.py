import os
from wifi import Cell, Scheme
import subprocess, json
path = "./"
data = open(path + "config.json",'r').read()
val = json.loads(data)
INTERFACE = val["INTERFACE"]
def connetWIFI(ssid, password, id):
    SAVE_CONFIG = "sudo wpa_cli  -i {} save_config".format(INTERFACE)
    SET_SSID = "sudo wpa_cli  -i {}  set_network {} ssid  '\"{}\"'".format(INTERFACE, id, ssid)
    os.system(SET_SSID)
    os.system(SAVE_CONFIG)
    SET_PASS = "sudo wpa_cli  -i {}  set_network {} psk   '\"{}\"'".format(INTERFACE, id, password)
    os.system(SET_PASS)
    os.system(SAVE_CONFIG)
    RESTART =  "sudo wpa_cli  -i {} reconfigure".format(INTERFACE)
    os.system(RESTART)
    # print(SET_SSID)
    # print(SET_PASS)
    # print(RESTART)

def getAllWifi():
    cell = Cell.all(INTERFACE)
    ssidLl = []
    cells = list(cell)
    for i in cells:
        ssidLl.append(i.ssid)
    return ssidLl

def getCurrentWifi():
    SSID = "--1-1"
    VAL = 0
    try:
        name = str(subprocess.check_output(['sudo', 'iwgetid']))
        name = name.split('"')[1]
        return 1, name
    except Exception as e:
        return -1, SSID

def combineWifi():
    ll = getAllWifi()
    fl = []
    VAL, CUR = getCurrentWifi()
    for i in ll:
        if i == "South-Pole":
            pass
        elif i == CUR:
            fl.append({"code" : 1, "ssid" : i, "del" : 0})
        else:
            fl.append({"code" : 0, "ssid" : i, "del" : 0})
    return fl


# combineWifi()
