from django.urls import path, include
from . import views
app_name= "Account"
urlpatterns =[path('sign_up/', views.sign_up, name="signup"),
path('log_in/', views.log_in, name="login"),
path('log_out/', views.log_out, name="logout")
]