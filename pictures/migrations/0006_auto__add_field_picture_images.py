# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Picture.images'
        db.add_column('cmslab_pictures', 'images',
                      self.gf('filebrowser.fields.FileBrowseField')(max_length=500, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Picture.images'
        db.delete_column('cmslab_pictures', 'images')


    models = {
        u'pictures.picture': {
            'Meta': {'object_name': 'Picture', 'db_table': "'cmslab_pictures'"},
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'images': ('filebrowser.fields.FileBrowseField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['pictures']