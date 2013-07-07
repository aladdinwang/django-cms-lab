from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import tests.urls

#from filebrowser.sites import site
import filebrowser.urls
from pagedesign.views import MasterPageSelectWizard
from pagedesign.forms import MasterPageSelectForm, RowsInfoForm
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cmslab.views.home', name='home'),
    # url(r'^cmslab/', include('cmslab.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       
    # Uncomment the next line to enable the admin:
    url(r'^media/gridfs/(?P<fpath>.*)$', 'pictures.views.gridfs'),
    ('^pages/', include('django.contrib.flatpages.urls')),
    url( r'^news/', include( 'demo.urls' ) ),
    url( r'^wizard/', include( 'django.contrib.formtools.tests.urls' ) ),
    url( r'^admin/masterpage/', MasterPageSelectWizard.as_view([ MasterPageSelectForm, RowsInfoForm ]) ),
    #url( r'^admin_tools/', include( 'admin_tools.urls' ) ),
    #url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^admin/filebrowser/', include(filebrowser.urls)),
    url( r'^admin/', include( admin.site.urls ) ),
    url( r'^', include( 'cms.urls' ) ),
    url( r'^tests/', include( tests.urls ) ),
) + static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )

urlpatterns += staticfiles_urlpatterns()
