from django.shortcuts import render
from django.contrib.auth.decorators import login_required



def lobby(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    return render(request, 'chat/home.html', {'title': 'Чатик'})
