from django.conf.urls import patterns, url

urlpatterns = patterns('demo.views',
                   url(r'create/$', 'publish' ),
                   url(r'latest/$', 'allnews' ),
                   url(r'show/$', 'show' ),
                   url(r'demo_photography/$', 'demo_photography'),
)


