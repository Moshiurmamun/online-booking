from django.urls import path, re_path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('sign-up/', views.RegistrationUser.as_view(), name='signup'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.logout_request, name="logout"),
    path('mydashboard/basic-info/', views.ChangeBasicInfo.as_view(), name='change-basic-info'),
    path('change/password/', views.ChangePassword.as_view(), name='change-password'),
    re_path('mydashboard/(?P<profile_id>[0-9]+)/$', views.profile, name="profile"),

]
