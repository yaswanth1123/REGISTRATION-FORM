import profile
from django.shortcuts import render
from app.forms import ProfileForm, UserForm
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect
from django.urls import reverse

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

            # send_mail('registration',
            # 'Registration is successfull',
            # 'yaswanthreddyyash7660@gmail.com',
            # [user1.email],
            # fail_silently=True)

            return HttpResponse('resigration is successful')    
    return render(request,"registration.html",d)

def home(request):
    if request.session.get('username'):
        d={'username':request.session.get('username')}
        return render(request,'home.html',d)
    return render(request,'home.html')


def user_login(request):
    if request.method=='POST':
        username=request.POST['un']
        password=request.POST['pw']

        user=authenticate(username=username, password=password)
        if user and user.is_active:
            login(request,user)
            request.session['username']=username
            return HttpResponseRedirect(reverse('home'))
    return render(request,'user_login.html')

@login_required
def user_logout(request):
    logout(request)

    return HttpResponseRedirect(reverse('home'))


@login_required
def display_details(request):
    username=request.session['username']
    ud=User.objects.get(username=username)
    pd=Profile.objects.get(user=ud)
    print(ud)
    d={'ud':ud,'pd':pd}
    return render(request,'display_details.html',d)

@login_required
def change_password(request):
    if request.method=='POST':
        nw=request.POST['nw']
        username=request.session['username']
        UO=User.objects.get(username=username)
        UO.set_password(nw)
        UO.save()
        return HttpResponse('changed successfully')
    return render(request,'change_password.html')


def reset_password(request):
    if request.method=='POST':
        rp=request.POST['rp']
        un=request.POST['un']
        ur=User.objects.filter(username=un)
        for i in ur:
            for j in User.objects.all():
                if i==j:
                    i.set_password(rp)
                    i.save()
        
        return HttpResponse('Reset password is successful')

    return render(request,'reset_password.html')



# def reset_password(request):
#     if request.method=='POST':
#         rp=request.POST['rp']
#         un=request.POST['un']
#         ur=User.objects.get(username=un)
#         ur.set_password(rp)
#         u.save()
#         return HttpResponse('Reset password is successful')

#     return render(request,'reset_password.html')