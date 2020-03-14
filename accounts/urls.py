from django.urls import path, re_path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('sign-up/', views.RegistrationUser.as_view(), name='signup'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.logout_request, name="logout"),
    path('mydashboard/basic-info/', views.ChangeBasicInfo.as_view(), name='change-basic-info'),
    path('change/password/', views.ChangePassword.as_view(), name='change-password'),

    #re_path('list-property/(?P<id>[0-9]+)/$', views.list_property, name="list_property"),
    re_path('create-property/(?P<user_id>[0-9]+)/$', views.create_property, name="create_property"),
    re_path('create-property/add-room/(?P<id>[0-9]+)/$', views.add_room, name="add_room"),

    re_path('mydashboard/(?P<profile_id>[0-9]+)/$', views.profile, name="profile"),
    re_path('mydashboard/view-room/(?P<id>[0-9]+)/$', views.view_all_rooms, name="view_all_rooms"),

    path('api/auth/facebook/<str:uid>/', views.SocialSigninApi.as_view(), name='fb_auth_api'),
]
