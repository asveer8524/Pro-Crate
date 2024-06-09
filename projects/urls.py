from django.urls import path
from . import views
from accounts.views import user_profile


urlpatterns=[
    path('createProject/', views.create_project, name='create_project'),
    path('bookmarkIt/', views.bookmarkIt, name='bookmarkIt'),
    path('addComment/', views.addComment, name='addComment'),
    path('/accounts/<username>/' ,user_profile, name='userProfile1'),
    path('<slug>/', views.projectDetail, name='projectDetail'),

]
