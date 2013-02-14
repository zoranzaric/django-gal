# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Image'
        db.create_table('gal_image', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('filename', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('gal', ['Image'])


    def backwards(self, orm):
        # Deleting model 'Image'
        db.delete_table('gal_image')


    models = {
        'gal.image': {
            'Meta': {'object_name': 'Image'},
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['gal']