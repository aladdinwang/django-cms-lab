import models
from django.contrib import admin


class PictureAdmin( admin.ModelAdmin ):
    list_display = ('filename', )
    search_fields = ('filename', 'image')
    def delete_model(self, request, obj):
        models.fs.delete(obj.image)
        super(PictureAdmin, self).delete_model(request, obj)
        


admin.site.register( models.Picture, PictureAdmin )
