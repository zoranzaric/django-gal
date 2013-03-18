# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Image.gallery_name'
        db.delete_column('gal_image', 'gallery_name')


    def backwards(self, orm):
        # Adding field 'Image.gallery_name'
        db.add_column('gal_image', 'gallery_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)


    models = {
        'gal.gallery': {
            'Meta': {'object_name': 'Gallery'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '255'})
        },
        'gal.image': {
            'Meta': {'object_name': 'Image'},
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gal.Gallery']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'picked': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['gal']