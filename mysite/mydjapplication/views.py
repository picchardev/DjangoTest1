from django.shortcuts import render
from django.http import HttpResponse

from . forms import RegistrationForm
from flask import Flask, render_template
from . import firebaseAuth

app = Flask(__name__)



def index(request):
    return render(request, "mydjapplication/index.html")


def add(request):
    val1 = int(request.GET["num1"])
    val2 = int(request.GET["num2"])
    res = val1 + val2
    return render(request,"mydjapplication/base.html", {'Result':res})


def MasterAdminLogin(request):
    uid = request.GET["userid"]
    pas = request.GET["password"]
    if firebaseAuth.MasterAdminLogin(uid,pas)==True:
        return render(request, "mydjapplication/base.html", {'Result': 'Welcome Admin'})
    else:
        return render(request, "mydjapplication/base.html", {'Result': 'Wrong'})


def getUserDetails(request):
    userDetails = firebaseAuth.viewAllUser()
    return render(request,"mydjapplication/userdetails.html",{'userlist':userDetails})