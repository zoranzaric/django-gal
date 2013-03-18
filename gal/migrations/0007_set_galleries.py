# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        for image in orm.Image.objects.all():
            try:
                gallery = orm.Gallery.objects.get(name=image.gallery_name)
            except orm.Gallery.DoesNotExist:
                gallery = orm.Gallery(name=image.gallery_name)
                gallery.save()
            image.gallery = gallery
            image.save()


    def backwards(self, orm):
        for image in orm.Image.objects.all():
            image.gallery_name = image.gallery.name
            image.save()

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
    symmetrical = True
