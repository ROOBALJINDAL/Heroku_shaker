from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse
from shaker.models import User
from django.template import RequestContext, loader
# Create your views here.
def home(request):
    my=""
    string= User.objects.all().order_by('-highscore')[:]
    for i in string:
        my=my+str(i)+"<br><br><br>"
    return HttpResponse(my)

def leaderboard(request):
    user_list=User.objects.all()
    template= loader.get_template("shaker/dashboard.html")
    data=RequestContext(request, {'key_to_html':user_list} )
    return HttpResponse(template.render(data))
