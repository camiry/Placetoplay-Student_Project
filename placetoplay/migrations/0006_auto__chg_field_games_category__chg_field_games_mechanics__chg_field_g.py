# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Games.category'
        db.alter_column(u'placetoplay_games', 'category', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Games.mechanics'
        db.alter_column(u'placetoplay_games', 'mechanics', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Games.image_path'
        db.alter_column(u'placetoplay_games', 'image_path', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Games.name'
        db.alter_column(u'placetoplay_games', 'name', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Games.date_published'
        db.alter_column(u'placetoplay_games', 'date_published', self.gf('django.db.models.fields.CharField')(max_length=15))

        # Changing field 'Games.optimal_age'
        db.alter_column(u'placetoplay_games', 'optimal_age', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'Games.comments'
        db.alter_column(u'placetoplay_games', 'comments', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Games.maker'
        db.alter_column(u'placetoplay_games', 'maker', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Games.average_rating'
        db.alter_column(u'placetoplay_games', 'average_rating', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=1))

        # Changing field 'Games.playtime'
        db.alter_column(u'placetoplay_games', 'playtime', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'Games.amount_owned'
        db.alter_column(u'placetoplay_games', 'amount_owned', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'Games.description'
        db.alter_column(u'placetoplay_games', 'description', self.gf('django.db.models.fields.TextField')())

    def backwards(self, orm):

        # Changing field 'Games.category'
        db.alter_column(u'placetoplay_games', 'category', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Games.mechanics'
        db.alter_column(u'placetoplay_games', 'mechanics', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Games.image_path'
        db.alter_column(u'placetoplay_games', 'image_path', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Games.name'
        db.alter_column(u'placetoplay_games', 'name', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Games.date_published'
        db.alter_column(u'placetoplay_games', 'date_published', self.gf('django.db.models.fields.CharField')(max_length=15, null=True))

        # Changing field 'Games.optimal_age'
        db.alter_column(u'placetoplay_games', 'optimal_age', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'Games.comments'
        db.alter_column(u'placetoplay_games', 'comments', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Games.maker'
        db.alter_column(u'placetoplay_games', 'maker', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Games.average_rating'
        db.alter_column(u'placetoplay_games', 'average_rating', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=1))

        # Changing field 'Games.playtime'
        db.alter_column(u'placetoplay_games', 'playtime', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'Games.amount_owned'
        db.alter_column(u'placetoplay_games', 'amount_owned', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'Games.description'
        db.alter_column(u'placetoplay_games', 'description', self.gf('django.db.models.fields.TextField')(null=True))

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'placetoplay.games': {
            'Meta': {'object_name': 'Games'},
            'amount_owned': ('django.db.models.fields.PositiveIntegerField', [], {'default': "'0'"}),
            'average_rating': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '5', 'decimal_places': '1'}),
            'category': ('django.db.models.fields.CharField', [], {'default': "'Board game'", 'max_length': '50'}),
            'comments': ('django.db.models.fields.TextField', [], {'default': "'This game has no comments yet.'"}),
            'date_published': ('django.db.models.fields.CharField', [], {'default': "' '", 'max_length': '15'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "'No description avaliable'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_path': ('django.db.models.fields.TextField', [], {'default': "'/static/mtg.jpeg'"}),
            'maker': ('django.db.models.fields.CharField', [], {'default': "' '", 'max_length': '50'}),
            'mechanics': ('django.db.models.fields.TextField', [], {'default': "'No data'"}),
            'name': ('django.db.models.fields.TextField', [], {'default': "'No name avaliable'"}),
            'optimal_age': ('django.db.models.fields.PositiveIntegerField', [], {'default': "'0'"}),
            'playtime': ('django.db.models.fields.PositiveIntegerField', [], {'default': "'0'"})
        },
        u'placetoplay.groups': {
            'Meta': {'object_name': 'Groups'},
            'address': ('django.db.models.fields.CharField', [], {'default': "'Placeholder address'", 'max_length': '60'}),
            'admin_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'games': ('django.db.models.fields.TextField', [], {'default': "'Probably never use this...'"}),
            'games_link': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'group games'", 'symmetrical': 'False', 'to': u"orm['placetoplay.Games']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_path': ('django.db.models.fields.CharField', [], {'default': "'/static/mtg.jpg'", 'max_length': '70', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '90'}),
            'phone': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'private_group': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'schedule_date': ('django.db.models.fields.DateField', [], {'default': "'2013-10-13'"}),
            'schedule_event': ('django.db.models.fields.TextField', [], {'default': "'Please check back soon for our first scheduled event!'"}),
            'schedule_time': ('django.db.models.fields.TimeField', [], {'default': "'00:00:00'"}),
            'skill_level': ('django.db.models.fields.CharField', [], {'default': "'No skill level selected'", 'max_length': '30'}),
            'special_rules': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'placetoplay.userextension': {
            'Meta': {'object_name': 'UserExtension'},
            'characteristics': ('django.db.models.fields.TextField', [], {'max_length': '255', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'facebook': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'friends': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'friends_rel_+'", 'to': u"orm['placetoplay.UserExtension']"}),
            'game_pref1': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'game_pref2': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'game_pref3': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'games_link': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'link_to_games'", 'symmetrical': 'False', 'to': u"orm['placetoplay.Games']"}),
            'group_link': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'members'", 'symmetrical': 'False', 'to': u"orm['placetoplay.Groups']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_path': ('django.db.models.fields.CharField', [], {'default': "'/static/mtg.jpg'", 'max_length': '100'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'skill': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'user_link': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'extension'", 'unique': 'True', 'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['placetoplay']