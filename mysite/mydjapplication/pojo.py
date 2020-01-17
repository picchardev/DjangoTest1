import json


class users:

    def __init__(self, id, mUserAboutMe, mUserDOB, mUserEmail, mUserFname, mUserGender, mUserId, mUserImgUrl,
                 mUserIndustry, mUserInterest, mUserLocation, mUserPass, mUserPhno, mUserWebSite, tokenId):
        super().__init__()
        self.userid = mUserId
        self.userfname = mUserFname
        self.usergender = mUserGender
        self.userdob = mUserDOB
        self.userimgurl = mUserImgUrl
        self.id = id
        self.useraboutme = mUserAboutMe
        self.useremail = mUserEmail
        self.userindustry = mUserIndustry
        self.userinterest = mUserInterest
        self.userlocation = mUserLocation
        self.userpass = mUserPass
        self.userphno = mUserPhno
        self.userwebsite = mUserWebSite
        self.usertoken = tokenId

    @classmethod
    def from_json(cls, json_string):
        json_string = json_string.replace("\'", "\"")
        json_dict = json.loads(json_string)
        return cls(**json_dict)

    def setId(self, id):
        self.id = id

    def set_userid(self, userid):
        self.userid = userid

    def set_useremail(self, useremail):
        self.useremail = useremail

    def set_userfname(self, userfname):
        self.userfname = userfname

    def set_useraboutme(self, useraboutme):
        self.useraboutme = useraboutme

    def set_usergender(self, usergender):
        self.usergender = usergender

    def set_userimgurl(self, userimgurl):
        self.userimgurl = userimgurl

    def set_userindustry(self, userindustry):
        self.userindustry = userindustry

    def set_userinterest(self, userinterest):
        self.userinterest = userinterest

    def set_userlocation(self, userlocation):
        self.userlocation = userlocation

    def set_userpass(self, userpass):
        self.userpass = userpass

    def set_userphno(self, userphno):
        self.userphno = userphno

    def set_userwebsite(self, userwebsite):
        self.userwebsite = userwebsite

    def set_usertoken(self, usertoken):
        self.usertoken = usertoken

    def set_userdob(self, userdob):
        self.userdob = userdob

    def getid(self):
        return self.id

    def getuserid(self):
        return self.userid

    def getuserfname(self):
        return self.userfname

    def getusergender(self):
        return self.usergender

    def getuserdob(self):
        return self.userdob

    def getuserimgurl(self):
        return self.userimgurl

    def getuseraboutme(self):
        return self.useraboutme

    def getuseremail(self):
        return self.useremail

    def getuserindustry(self):
        return self.userindustry

    def getuserinterest(self):
        return self.userinterest


class MasterAdmin:

    def __init__(self, UserId, Password):
        self.UserId = UserId
        self.Password = Password

    @classmethod
    def Madmin_from_json(cls, json_string):
        json_string = json_string.replace("\'", "\"")
        json_dict = json.loads(json_string)
        return cls(**json_dict)









