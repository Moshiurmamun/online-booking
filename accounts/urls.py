from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('sign-up/', views.RegistrationUser.as_view(), name='signup'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.logout_request, name="logout"),

]
