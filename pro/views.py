from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from accounts.models import Profile
from projects.models import project_data
from django.views.decorators.csrf import csrf_exempt,csrf_protect




def getUserList(s_key):
    return Profile.objects.values().filter(username__contains=s_key)

def getProjectList(s_key):
    return project_data.objects.values().filter(title__contains=s_key)

def getBlogList(s_key):
    return {'no_data':'coming soon'}



@csrf_exempt
def search(request):
    s_user_flag=False;
    s_blog_flag=False;
    s_project_flag=False;


    print(request.method)
    #context = {'search_flag':search_flag}
    if request.method == "POST" :
        s_key = request.POST.get('search')
        s_opt = request.POST.get('options')
        print(request.POST)

        if s_opt == 'user':
            search_result = getUserList(s_key)
            s_user_flag = True;
        elif s_opt == 'project':
            search_result = getProjectList(s_key)
            s_project_flag = True;
        elif s_opt == 'blog':
            search_result = getBlogList(s_key)
            s_blog_flag = True;


        print(search_result)
        context = {'search_result':search_result,'s_user_flag':s_user_flag,'s_project_flag':s_project_flag,'s_blog_flag':s_blog_flag,'s_key':s_key,'s_opt':s_opt}

        return render(request,"search.html", context)
    else:
        search_result = ""
        s_key = request.GET.get('search')
        s_opt = request.GET.get('options')
        print(request.GET)

        if s_opt == 'user':
            search_result = getUserList(s_key)
            s_user_flag = True;
        elif s_opt == 'project':
            search_result = getProjectList(s_key)
            s_project_flag = True;
        elif s_opt == 'blog':
            search_result = getBlogList(s_key)
            s_blog_flag = True;


        print(search_result)
        context = {'search_result':search_result,'s_user_flag':s_user_flag,'s_project_flag':s_project_flag,'s_blog_flag':s_blog_flag,'s_key':s_key,'s_opt':s_opt}

        return render(request,"search.html", context)
        #return HttpResponse("Some error occured")
        #return render(request,"search.html", context)



def homepage(request):
    name=''
    projects=''
    a=''
    if request.user.is_authenticated:
        print("User loggedin :" + str(request.user))
        a = Profile.objects.get(username=request.user)
        name = a.name
        #print(a.name)

        projects = project_data.objects.values().filter(owner1 = request.user )



        #print(projects)
    return render(request,'homepage.html',{'name':name,'projects':projects,'profile':a})


def test(request):
    return render(request,'test.html')
