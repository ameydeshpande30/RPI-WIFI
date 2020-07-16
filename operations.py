import os
from wifi import Cell, Scheme
import subprocess


INTERFACE = "wlp3s0"
def connetWIFI(ssid, password):
    SET_SSID = "sudo wpa_cli  -i {}  set_network 0 ssid  '\"{}\"'".format(INTERFACE, ssid)
    os.system(SET_SSID)
    SET_PASS = "sudo wpa_cli  -i {}  set_network 0 psk   '\"{}\"'".format(INTERFACE, password)
    os.system(SET_PASS)
    RESTART =  "sudo wpa_cli  -i {} reconfigure".format(INTERFACE)
    os.system(RESTART)

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
            fl.append({"code" : 1, "ssid" : i})
        else:
            fl.append({"code" : 0, "ssid" : i})
    return fl


# combineWifi()
