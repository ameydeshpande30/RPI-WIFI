from peewee import *
path = "./"
db = SqliteDatabase(path + 'wifiData.db')

class BaseModel(Model):
    class Meta:
        database = db

class Networks(BaseModel):
    id = AutoField()
    ssid = CharField(max_length=5000, unique=True)
    password = CharField(max_length=5000)


db.connect()
db.create_tables([Networks])

def addNetwrok(ssid, password):
    Networks.create(ssid=ssid, password=password)
    db.commit()

def getAllNetwork():
    ll = Networks.select()
    fl = []
    for i in ll:
        fl.append({"ssid" : i.ssid, "password" : i.password})
    return fl

def getPassword(ssid):
    try:
        network = Networks.select().where(Networks.ssid == ssid).get()
        passs = network.password
        return 1, passs
    except Exception as e:
        # print(e)
        return -1, "no password"


def changePassword(ssid, password):
    try:
        network = Networks.select().where(Networks.ssid == ssid).get()
        network.password = password
        print(network.password)
        network.save()
        db.commit()
        return 1
    except Exception as e:
        # print(e)
        return -1
