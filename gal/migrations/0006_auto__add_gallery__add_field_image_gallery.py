# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Gallery'
        db.create_table('gal_gallery', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', unique=True, max_length=255)),
        ))
        db.send_create_signal('gal', ['Gallery'])

        # Adding field 'Image.gallery'
        db.add_column('gal_image', 'gallery',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gal.Gallery'], null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Gallery'
        db.delete_table('gal_gallery')

        # Deleting field 'Image.gallery'
        db.delete_column('gal_image', 'gallery_id')


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
            'gallery_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'picked': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['gal']
