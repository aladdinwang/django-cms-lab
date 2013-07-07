from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns( views.hello,
    url( r'^tests/test_formsubmit/$', views.test_formsubmit ),
)
