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

def index(request):
    user = request.user

    context = {
        "user": user,
    }
    return render(request,"gestioncolloque/index.html", context)

def about(request):
    user = request.user

    context = {
        "user": user,
    }
    return render(request,"gestioncolloque/about.html", context)

def gallery(request):
    user = request.user

    context = {
        "user": user,
    }
    return render(request,"gestioncolloque/gallery.html", context)

def faq(request):
    user = request.user

    context = {
        "user": user,
    }
    return render(request,"gestioncolloque/faq.html", context)

def pricing(request):
    user = request.user

    context = {
        "user": user,
    }
    return render(request,"gestioncolloque/pricing.html", context)

def sponsors(request):
    user = request.user

    context = {
        "user": user,
    }
    return render(request,"gestioncolloque/sponsors.html", context)

def venue(request):
    user = request.user

    context = {
        "user": user,
    }
    return render(request,"gestioncolloque/venue.html", context)

def speakers(request):
    user = request.user

    context = {
        "user": user,
    }
    return render(request,"gestioncolloque/speakers.html", context)

def schedule(request):
    user = request.user

    context = {
        "user": user,
    }
    return render(request,"gestioncolloque/schedule.html", context)

def blog(request):
    user = request.user

    context = {
        "user": user,
    }
    return render(request,"gestioncolloque/blog.html", context)

def blog_detail(request):
    user = request.user

    context = {
        "user": user,
    }
    return render(request,"gestioncolloque/blog-detail.html", context)


def contact(request):
    user = request.user

    context = {
        "user": user,
    }
    return render(request,"gestioncolloque/contact.html", context)



@user_passes_test(is_not_superuser)
@login_required
def dashboard(request):
    user = request.user


    context = {
        "user": user,
    }
    return render(request,"gestioncolloque/dashboard.html", context)

@user_passes_test(is_not_superuser)
@login_required
def profile(request):
    user = request.user

    
    context = {
        "user": user,
    }
    return render(request,"gestioncolloque/profile.html", context)

