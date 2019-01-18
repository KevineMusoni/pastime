from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    # landing page
    url('^$',views.pastime,name = 'pastime'),
    #search results page 
    url(r'^search/', views.search_results, name='search_results'),
    # link to the sport details
    url(r'^sport/(\d+)',views.sport,name='sport'),
    url(r'^allsports/',views.allsports,name='allsports'),
    url(r'^myaccount/$', views.mine, name='myaccount'),
    url(r'^myaccount/edit/$', views.edit, name='edit')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)