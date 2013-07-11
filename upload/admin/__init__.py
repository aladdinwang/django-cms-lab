# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _
from models import ZipUpload
from forms import ZipUploadForm

import zipfile

class ZipUploadAdmin( admin.ModelAdmin ):
    def changelist_view( self, request, extra_context=None ):
        submit_row_template = '<div class="submit-row">\n  %s\n</div>'
        if request.method == 'POST':
            form = ZipUploadForm( request.POST, request.FILES )
            if form.is_valid():
                fp = request.FILES['zipfile']
                with zipfile.ZipFile(fp) as uploadzip:
                    print uploadzip.namelist()
                    uploadzip.extractall( settings.MEDIA_ROOT )
                """
                with open('/tmp/test', 'w') as test:
                    for chunk in fp.chunks():
                        test.write( chunk )
                """
            submit_buttons = []
            button_template = '<input type="button" value="%s" onclick="javascript:location.href=%s"/>'
            submit_buttons.append( button_template % ( _( 'Back' ), '\'/admin/cms/zipupload/\'' ) )
            submit_buttons.append( button_template % ( _( 'Browse'), '\'/admin/filebrowser/browse/\'' ) )
                      
            context = {
                'title': _('Upload Successfully'),
                'has_file_field': 1,
                'buttons': mark_safe( '\n'.join( submit_buttons ) )
            }
            return render_to_response( 'forms/upload.html', 
                                   RequestContext( request, context ))
        else:
            form = ZipUploadForm()
                
        submit_button =  '<input type="submit" name="_save" class="default" value="%s" />' % _('Save')
        
        context = {
            'form': form,
            'has_file_field': 1,
            'buttons': mark_safe( submit_row_template % submit_button )
            }
        return render_to_response( 'forms/upload.html', 
                                   RequestContext( request, context ))
        
    def has_add_permission( self, request ):
        return False

admin.site.register( ZipUpload, ZipUploadAdmin )
