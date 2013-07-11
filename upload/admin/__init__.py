# -*- coding: utf-8 -*-
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import ZipUpload
from forms import ZipUploadForm


class ZipUploadAdmin( admin.ModelAdmin ):
    def changelist_view( self, request, extra_context=None ):
        if request.method == 'POST':
            form = ZipUploadForm( request.POST, request.FILES )
            if form.is_valid():
                fp = request.FILES['zipfile']
                with open('/tmp/test', 'w') as test:
                    for chunk in fp.chunks():
                        print chunk
                        test.write( chunk )
            return HttpResponse( unicode( 'ok' ) )    
        else:
            form = ZipUploadForm()
        submit_row_template = '<div class="submit-row>\n"  %s\n</div>'
        submit_button =  '<input type="submit" name="_save" class="default" value="{% trans "Save" %}" {{ onclick_attrib }}/>'
        print submit_row_template %  submit_button
        context = {
            'form': form,
            'has_file_field': 1,
            'buttons': submit_row_template % submit_button
            }
        return render_to_response( 'forms/upload.html', 
                                   RequestContext( request, {'form': form, 'has_file_field': 1 } ))
        
    def has_add_permission( self, request ):
        return False

admin.site.register( ZipUpload, ZipUploadAdmin )
