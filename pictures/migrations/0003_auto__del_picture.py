# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Picture'
        db.delete_table(u'pictures_picture')


    def backwards(self, orm):
        # Adding model 'Picture'
        db.create_table(u'pictures_picture', (
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('filename', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'pictures', ['Picture'])


    models = {
        
    }

    complete_apps = ['pictures']