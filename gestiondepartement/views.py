from django.http import HttpResponse, HttpResponseBadRequest, FileResponse, Http404, HttpResponseForbidden
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.template import loader
from mimetypes import guess_type
from django.urls import resolve
from django.db.models import Sum, Q, F, Value
from django.db.models.functions import Coalesce
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
import requests
from django.utils.timezone import now

# import pywhatkit

def is_not_superuser(user):
    return user.is_superuser == False


def home(request):
    user = request.user

    context = {
        "user": user,
    }
    return render(request,"gestiondepartement/index.html", context)

def contribuer(request):
    user = request.user

    context = {
        "user": user,
    }
    return render(request,"gestiondepartement/contribuer.html", context)

def apropos(request):
    user = request.user

    context = {
        "user": user,
    }
    return render(request,"gestiondepartement/apropos.html", context)

def missions(request):
    user = request.user

    context = {
        "user": user,
    }
    return render(request,"gestiondepartement/missions.html", context)

def faits(request):
    user = request.user

    context = {
        "user": user,
    }
    return render(request,"gestiondepartement/faits.html", context)

@user_passes_test(is_not_superuser)
@login_required
def dashboard(request):
    user = request.user


    context = {
        "user": user,
    }
    return render(request,"gestiondepartement/dashboard.html", context)

@user_passes_test(is_not_superuser)
@login_required
def profile(request):
    user = request.user

    
    context = {
        "user": user,
    }
    return render(request,"gestionadmin/profile.html", context)

