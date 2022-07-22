import profile
from django.shortcuts import render
from app.forms import ProfileForm, UserForm
from django.http import HttpResponse

# Create your views here.
from app.models import *

def registration(request):
    UF=UserForm()
    PF=ProfileForm()
    d={'UF':UF,'PF':PF}
    if request.method=='POST' and request.FILES:
        UD=UserForm(request.POST)
        PD=ProfileForm(request.POST,request.FILES)
        if UD.is_valid() and PD.is_valid():
            user1=UD.save(commit=False)
            user1.set_password(UD.cleaned_data['password'])
            user1.save()
            profile=PD.save(commit=False)
            profile.user=user1
            profile.save()

            send_mail('registration',
            'Registration is successfull',
            'yaswanthreddyyash7660@gmail.com',
            [user1.email],
            fail_silently=True)

            return HttpResponse('resigration is successful')
            

        
    return render(request,"registration.html",d)
