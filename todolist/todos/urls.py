from django.conf.urls import url
from . import views

urlpatterns=[

url(r'^$',views.index,name='index'),
# url(r'^$', 'homefood.views.home', name='home'),
url(r'^details/(?P<id>\w{0,50})/$',views.details),
url(r'^add', views.add, name='add'),
url(r'^edit/(?P<id>\d{0,50})/$', views.edit, name='edit'),
url(r'^delete/(?P<id>\d{0,50})/$', views.delete, name='delete')

]
