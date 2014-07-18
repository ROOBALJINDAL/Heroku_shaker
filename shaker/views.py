from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse
from shaker.models import User
# Create your views here.
def home(request):
    my=""
    string= User.objects.all().order_by('highscore')[:4]
    for i in string:
        my=my+str(i)+"<br>"
    return HttpResponse(my)
