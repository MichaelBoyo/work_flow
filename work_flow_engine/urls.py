from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.sign_up),
    path('send_email/', views.send_email),
    path('userpage/', views.userpage),
    path('automate/', views.automate),
    path('autoresponder/', views.autoresponder),
    path('ec_mktn/', views.ecommerce),
    path('blank/', views.blank),
]
