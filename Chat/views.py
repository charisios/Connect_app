from django.shortcuts import render, redirect
from .models import Room, Message
from django.http import HttpResponse, JsonResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')


def checkview(request):
    room = request.POST['room_name']
    user = request.POST['username']

    if Room.objects.filter(room=room).exists():
        return redirect(f'/{room}/?username={user}')
    else:
        new_room = Room.objects.create(room=room)
        new_room.save()
        return redirect(f'/{room}/?username={user}')

def room(request, room):
    username= request.GET.get('username')
    room_details= Room.objects.get(room=room)

    return render(request, 'room.html', {'username':username, 'room':room, 'room_details':room_details})

def send(request):
    message= request.POST['message']
    user= request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(message=message, room=room_id, user=user)
    new_message.save()
    return HttpResponse('Message sent succesfully')

def getMessages(request, room):
    room = Room.objects.get(room=room)
    messages = Message.objects.filter(room=room.id)

    return JsonResponse({'messages':list(messages.values())})