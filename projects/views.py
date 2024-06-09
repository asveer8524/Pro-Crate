from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.contrib.auth.decorators import login_required
from . import forms
from accounts.models import Profile
from .models import project_data
from utility.models import bookmarks, comments
from utility.forms import post_comment



# Create your views here.
@csrf_exempt
@login_required()
def create_project(request):
    print(type(request.user))

    if request.method == 'POST':
        form = forms.create_project(request.POST,request.FILES)

        if form.is_valid():
            print("Valid project data")
            instance = form.save(commit=False)
            print('request.user')

            instance.owner = Profile.objects.get(username=str(request.user))
            instance.owner1 = str(request.user)
            instance.save()
            #return redirect('homepage')
            return projectDetail(request,instance.slug)
        else:
            print("Invalid form data")
            return HttpResponse("Invalid Form data, go back <br> <li> Try changing slug field </li>")
    else:

        form = forms.create_project()
        return render(request, 'projects/project_upload.html',{'form':form})

@csrf_exempt
def projectDetail(request,slug):
    project = get_object_or_404(project_data,slug = slug)
    #return HttpResponse(project.title)
    cmnt = post_comment()
    print(cmnt)

    allComments = comments.objects.values().filter(comment_on_slug = slug)

    return render(request,'projects/project_detail.html',{'project':project,'cmnt_form':cmnt, 'comments':allComments})

@csrf_exempt
def bookmarkIt(request):
    if request.method == 'POST':
        p_data = project_data.objects.get(slug = request.POST['slug'])

        if str(request.user) == str(p_data.owner1):
            print("both are same")
            return HttpResponse("You cannot bookmark your own project")
        else:

            instance = bookmarks(
                    bookmark_slug  = p_data,
                    bookmark_title = request.POST['title'],
                    username = request.user,
                    slug = request.POST['slug'],
                    owner = str(request.user)
                    )
            instance.save()
            print(instance)
            return HttpResponse("Surprise")
    else:
        return HttpResponse("Some error tooke place @bookmarkIt")

@csrf_exempt
def addComment(request):
    if request.method=='POST':
        instance = comments(
                comment_field = request.POST['comment_field'],
                comment_on_slug = request.POST['slug'],
                comment_by = request.user,
                owner = str(request.user)
                        )
        instance.save()
        print(instance)
        print("instance hopefully saved")

        return projectDetail(request,request.POST['slug'])
