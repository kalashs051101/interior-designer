from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    # path("",homepage,name="homepage"),
    path('',userregister,name='home'),
    path('accounts-login/',userlogin,name='login'),
    path("accounts-logout/",userlogout,name='logout'),
    # path('pro/',showproject,name='showproject'),
    path("user-update<int:index>/",userupdate,name="updatedata"),
    path('project-upload<str:index>/',uploadproject,name='uploadproject'),
    path("username",user_name,name="user_name"),

    path("accounts-projects/",showp,name='project'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)