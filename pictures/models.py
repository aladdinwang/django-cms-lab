from django.db import models
from django.utils.translation import ugettext_lazy as _

from filebrowser.fields import FileBrowseField
from mongoengine import *
import mongoengine.django.storage

connect('local')
fs = mongoengine.django.storage.GridFSStorage()


class Picture( models.Model ):
    filename = models.CharField( _( 'file name' ), max_length = 100, blank = True )
    # upload_to is the fake description
    images = FileBrowseField(_("FileBrowseField"), max_length = 500, blank = True, 
                             extensions = [".jpg", ".png", ".jpeg"], directory = 'gridfs/', null = True, format = "Image")
    image = models.ImageField( _( "mongoengine admin integrated" ), upload_to="gridfs", 
                               storage=fs )
    class Meta:
        db_table = 'cmslab_pictures'
