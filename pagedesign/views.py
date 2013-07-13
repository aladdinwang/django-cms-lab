# Create your views here.
from utils.conf import update_tuple_list

from cms.models import CMS_Template
from cms.utils.conf import get_extend_cfg, get_cms_templates

from pagedesign.forms import MasterPageSelectForm, RowsInfoForm

from django.http import HttpResponse
from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.formtools.wizard.views import SessionWizardView
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.template.loader import get_template, render_to_string
from django.utils.safestring import mark_safe
from django.template import Context

from configobj import ConfigObj, unrepr

import os


class MasterPageSelectWizard( SessionWizardView ):
    picture_row_snippet_choices = (
        ( 2, _('Picture with 2 columns') ),
        ( 3, _('Picture with 3 columns') ),
        )
    base_template_name = "base/photography.html"
    def done( self, form_list, **kwargs ):
        placeholder_template = " placeholder %(placeholder_name)s group=image tips=\"%(placeholder_tips)s\" " \
            "width=216 height=168 "
        cleaned_data = self.get_all_cleaned_data()
        #print cleaned_data
        row_count = int( cleaned_data.get( 'rows', 0 ) )
        picture_rows = []
        picture_id = 1
        col_ids = []
        for row in range( 1, row_count + 1 ):
            key = 'row' + str( row )
            # may use get
            picture_cols = []
            col_ids.append( cleaned_data[ key] )
            col_count = int( cleaned_data[ key ] )
            for col in range( 0, col_count  ):
                picture = {}
                substitution = {
                    'placeholder_name':  "photo%s" % str( picture_id ),
                    'placeholder_tips':  "Design for photo%s" % ( str( picture_id ) ),
                }
                picture_id += 1
                

                picture[ 'placeholder' ] = mark_safe( "{%" + placeholder_template % substitution \
                    + "%}" )
                picture[ 'url' ] = '#'
                picture[ 'name' ] = substitution[ 'placeholder_name' ]
                picture_cols.append( picture )
                
            picture_rows.append( picture_cols )
        

        template = render_to_string( self.base_template_name, Context( { 'picture_rows': picture_rows, 'template': 1 } ) )
        template =  mark_safe( template )
        
        #prepare template_name
        template_name_template = "photography_%s"
        for i in range( 0, row_count ):
            template_name_template += "_%s"
            ids = tuple( [ unicode(row_count) ] +  col_ids ) 
        template_name = template_name_template % ids
        
        templates_dir = os.path.join( settings.PROJECT_PATH, 'templates')
        template_path = os.path.join( templates_dir, template_name )
  
        """
        fp = open( template_path + '.html', 'w' )
        fp.write( template )
        fp.close()
        """
        # setting the config file
        config = get_extend_cfg()
        cms_templates = unrepr( config[ 'CMS_TEMPLATES' ] )
        
        update_tuple_list( cms_templates, template_path  + ".html", template_name )
        config[ 'CMS_TEMPLATES' ] = repr( cms_templates )
        config.write()

        page_addview_url = reverse('admin:cms_page_add')
        #Todo: generate the template and insert value to database
        template_upload_root = 'media/templates'
        filename = cleaned_data[ 'filename' ]
        filename = os.path.join( template_upload_root, filename + '.html' )
        full_path = os.path.join( settings.PROJECT_PATH, filename )
        
  

        cms_templates = CMS_Template.objects.filter( cms_template = filename )
        
        cms_template = None
        if not len(cms_templates):
            cms_template = CMS_Template(name = cleaned_data[ 'filename' ], cms_template = filename )
        else:
            cms_template = cms_templates[0]
        if os.path.exists( full_path ):
            print "Already exists"
        
        fp = open( full_path, 'w' )
        fp.write( template )
        fp.close()
        
        cms_template.save()
        
        #Todo: auto selected the new added template

        return HttpResponseRedirect( page_addview_url  )
    def get_form( self, step = None, data = None, files = None ):
        if '1' == step:
            raw_data = self.storage.get_step_data( '0' )
            count = raw_data.get( '0-rows', 0 )
            count = int(count)
            
            if not count:
                form.fields['wrongfield'] = forms.CharField( label = 'Something wrong' )
            else:
                form_class = RowsInfoForm
                form_class.base_fields.clear()
                for i in range( 1, count + 1 ):
                    name = 'row' + str( i )
                    label = 'Row ' + str( i )
                    form_class.base_fields[name] = forms.ChoiceField( label = label, choices = MasterPageSelectWizard.picture_row_snippet_choices )
                self.form_list['1'] = form_class

        form = super( MasterPageSelectWizard, self ).get_form( step, data, files )
        return form

 
