from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'(?P<symbol_code>.*)/$', views.question, name='question')
]
