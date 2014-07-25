from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse
from shaker.models import User
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def home(request):
    my=""
    string= User.objects.all().order_by('-highscore')[:]
    for i in string:
        my=my+str(i)+"<br><br><br>"
    return HttpResponse(my)

@csrf_exempt
def leaderboard(request):
    user_list=User.objects.all().order_by('-highscore')[:10]
    template= loader.get_template("shaker/dashboard.html")
    i = 1
    users = []
    for user in user_list:
        users.add({'rank': i, 'username': user.username, 'highscore':user.highscore})
        i = i + 1
    
    data=RequestContext(request, {'key_to_html':user_list} )
    return HttpResponse(template.render(data))
