from django.urls import path
from . import views
app_name="accounts"

urlpatterns=[
path('signup/', views.views_signup, name='signup'),
    path('login/', views.views_login, name='login'),
    path('logout/', views.views_logout, name='logout'),
    path('createProfile/', views.create_profile, name='create_profile'),
    path('<username>', views.user_profile, name='userProfile2'),
]
