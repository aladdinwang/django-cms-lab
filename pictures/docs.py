from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from mongoengine import *

connect('localhost')


class Picture( Document ):
    filename = StringField()
    image = ImageField( _( "mongoengine admin integrated" ) )
    
class PictureAdmin( admin.ModelAdmin ):
    pass

admin.site.register( Picture, PictureAdmin )
