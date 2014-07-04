from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers, viewsets
from shaker.models import User

class UserViewSet(viewsets.ModelViewSet):
    model=User

router = routers.DefaultRouter()
router.register(r'mygame/highscore',UserViewSet)


urlpatterns = [
    # Examples:
    # url(r'^$', 'pythonsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^',include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
]

