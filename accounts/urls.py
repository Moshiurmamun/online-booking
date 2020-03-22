from django.urls import path, re_path
from . import views

from booking.views import notifications


app_name = 'accounts'

urlpatterns = [
    path('sign-up/', views.RegistrationUser.as_view(), name='signup'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.logout_request, name="logout"),
    path('mydashboard/basic-info/', views.ChangeBasicInfo.as_view(), name='change-basic-info'),
    path('change/password/', views.ChangePassword.as_view(), name='change-password'),

    #re_path('list-property/(?P<id>[0-9]+)/$', views.list_property, name="list_property"),

    # ==============================================================================
    # =================================== Agent Profile=============================
    # ==============================================================================
    re_path('mydashboard/(?P<profile_id>[0-9]+)/$', views.profile, name="profile"),
    re_path('mydashboard/view-room/', views.view_all_rooms, name="view_all_rooms"),
    re_path('mydashboard/edit-property/(?P<hotel_id>[0-9]+)/$', views.edit_property, name="edit_property"),
    re_path('mydashboard/edit-room/(?P<room_id>[0-9]+)/$', views.edit_room, name="edit_room"),
    path('mydashboard/booking-details/', views.booking_details, name="booking_details"),
    re_path('mydashboard/notifications/(?P<p_id>[0-9]+)/$', notifications, name="notifications"),

    # Create Property
    re_path('create-property/(?P<user_id>[0-9]+)/$', views.create_property, name="create_property"),
    re_path('create-property/add-room/', views.add_room, name="add_room"),


    # ===================================================
    # =================Facebook Login ===================
    path('api/auth/facebook/<str:uid>/', views.SocialSigninApi.as_view(), name='fb_auth_api'),

]
