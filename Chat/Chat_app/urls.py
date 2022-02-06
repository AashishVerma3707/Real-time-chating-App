


from django.urls import path

from . import views
app_name= "App"

urlpatterns =[path('', views.home, name="homepage"),
path('<str:room>/',views.room, name="check"),
path('check',views.check, name="check"),
path('send',views.send, name="send"),
path('get_messages/<str:rroom>/',views.getmessages, name="getmessages")
            ]
