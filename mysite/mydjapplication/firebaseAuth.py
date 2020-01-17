import pyrebase
from . import pojo

config = {
    "apiKey": "7fc820d1958d3f7853550865f107981dd879416b",
    "authDomain": "auth-47c35.firebaseapp.com",
    "databaseURL": "https://auth-47c35.firebaseio.com/",
    "storageBucket": "auth-47c35.appspot.com",
    "serviceAccount": "E:/auth-47c35-firebase-adminsdk-j5pze-7fc820d195.json"
}

firebase = pyrebase.initialize_app(config)


def MasterAdminLogin(userid,pas):
    myStorageRef = firebase.storage()
    # myDatabaseRef = firebase.database().child('/UserRegData')
    myDatabaseRef = firebase.database().child('/Admin')

    snapshot = myDatabaseRef.get()
    #print(snapshot.val().items())

    # pojo.MasterAdmin.Madmin_from_json(str(snapshot.val().items()))

    values = []
    ResUserId = ''
    ResPass = ''

    for key, val in snapshot.val().items():
        print(str(val))
        values.append(pojo.MasterAdmin.Madmin_from_json(str(val)))

    for val in values:
        ResUserId = val.UserId
        ResPass = val.Password

    print("RUserid = ",ResUserId,"RPassword = ",ResPass)
    print("UUserId =",userid,"UPass =", pas)

    if ResPass.__eq__(pas) and ResUserId.__eq__(userid):
        print("match")
        return True
    else:
        return False


def viewAllUser():
    myDatabaseRef = firebase.database().child('/UserRegData')
    snapshot = myDatabaseRef.get()

    values = []

    for key, val in snapshot.val().items():
        values.append(pojo.users.from_json(str(val)))

    return values








