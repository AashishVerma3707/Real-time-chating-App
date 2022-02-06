
from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from .models import Room,Message
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required(login_url="/Account/log_in")
def home(request):
    return render(request,"index1.html",{"User":User})



def room(request,room):
    # user1 = User.objects.get(username=)
    user_name= request.GET.get("user1name")
    room_detail= Room.objects.get(Name=room)

    if Message.objects.filter(room=room_detail.id):
        t=None
    else:
        t=1

    return render(request, "index2.html",{"username":user_name,"room_details":room_detail,"room":room,"t":t})


def check(request):
    username = request.POST["user_name"]
    room_name = request.POST["room_name"]
    if Room.objects.filter(Name=room_name).exists():
        return redirect("/chat/"+room_name+"/?user1name="+ username)
    else:
        new_room = Room.objects.create(Name=room_name)
        new_room.save()
        return redirect("/chat/" + room_name + "/?user1name=" + username)


def send(request):
    username=request.POST['username']
    room_id=request.POST['room_id']
    message=request.POST['message']

    new_message= Message.objects.create(Value=message,  User=username , room=room_id)
    new_message.save()
    return HttpResponse("Message sent")


def getmessages(request,rroom):
    room_details= Room.objects.get(Name=rroom)
    if Message.objects.filter(room=room_details.id):
        messages= Message.objects.filter(room=room_details.id)
        return JsonResponse({"messages":list(messages.values())})
    else:
        return None
