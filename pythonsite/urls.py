from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers, viewsets
from shaker.models import User
from shaker import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from shaker import views

class UserViewSet(viewsets.ModelViewSet):
    model=User

router = routers.DefaultRouter()
router.register(r'mygame/highscore',UserViewSet)

admin.autodiscover() 

urlpatterns = [
    url(r'^',include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    #home ->  ^/
    
    url(r'^scoreboard/', views.leaderboard),
    url(r'^leaderboard/', views.json_leaderboard),
   
    url(r'^views/',views.home),
]

urlpatterns += staticfiles_urlpatterns()

