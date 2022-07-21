from django.shortcuts import render
from app.forms import ProfileForm, UserForm

# Create your views here.
from app.models import *

def registration(request):
    UF=UserForm()
    PF=ProfileForm()
    d={'UF':UF,'PF':PF}
    
    return render(request,"registration.html",d)
