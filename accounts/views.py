from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.contrib.auth.decorators import login_required
from . import forms
from .models import Profile
from projects.models import project_data
from utility.models import bookmarks


# User.objects.filter(username__contains="id")


def user_profile(request,username):

    myBookmarks=""
    user1 = get_object_or_404(Profile, username=username)
    projects = project_data.objects.values().filter(owner1 = user1.username)
    myBookmarks = bookmarks.objects.values().filter(owner = user1.username)

    print(myBookmarks)
    context={'user1':user1,'projects':projects, 'bookmarks':myBookmarks}
    return render(request,'accounts/userProfile.html', context)


# Create your views here.
@csrf_exempt
def views_signup(request):
    if request.method == 'POST':
        print("received signup data")
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print("Valid form")
            user = form.save()
            login(request, user)
            return redirect('/accounts/createProfile/')
    else:
        form = UserCreationForm()
    return render(request,'accounts/signup.html', {'form':form})

@csrf_exempt
def views_login(request):
    if request.method=='POST':
        print(request.POST)

        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            print("user logged in")
            #return redirect('homepage')
            return user_profile(request, user.username)
            print(form)
    else:
        form = AuthenticationForm()
        print(form)
    return render(request,'accounts/login.html', {'form':form})

@csrf_exempt
def views_logout(request):
    #print(request.method)
    if request.method == 'GET':
        print("logout called")
        logout(request)
        return redirect('homepage')
    else:
        return HttpResponse('Error occured')
        #return redirect('homepage')

@csrf_exempt
@login_required()
def create_profile(request):
    if request.method == 'POST':
        form = forms.addProfile(request.POST, request.FILES)

        if form.is_valid():
            print("Valid profile data")
            instance = form.save(commit=False)
            instance.user = request.user
            instance.username = str(request.user)
            instance.save()
            return redirect('homepage')
    else:
            form = forms.addProfile()
            return render(request,'accounts/addProfile.html',{'form':form})
