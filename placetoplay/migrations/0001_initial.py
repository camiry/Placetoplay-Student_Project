# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Games'
        db.create_table(u'placetoplay_games', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('maker', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('mechanics', self.gf('django.db.models.fields.TextField')()),
            ('date_published', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('rating', self.gf('django.db.models.fields.IntegerField')()),
            ('amount_owned', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('optimal_players', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('comments', self.gf('django.db.models.fields.TextField')(default='FUCK SOUTH')),
            ('image_path', self.gf('django.db.models.fields.TextField')(default='/static/mtg.jpeg')),
        ))
        db.send_create_signal(u'placetoplay', ['Games'])

        # Adding model 'Groups'
        db.create_table(u'placetoplay_groups', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=90)),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(default='Placeholder address', max_length=60)),
            ('games', self.gf('django.db.models.fields.TextField')(default='Probably never use this...')),
            ('special_rules', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('skill_level', self.gf('django.db.models.fields.CharField')(default='No skill level selected', max_length=30)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('phone', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('schedule_date', self.gf('django.db.models.fields.DateField')(default='2013-10-13')),
            ('schedule_time', self.gf('django.db.models.fields.TimeField')(default='00:00:00')),
            ('schedule_event', self.gf('django.db.models.fields.TextField')(default='Please check back soon for our first scheduled event!')),
            ('image_path', self.gf('django.db.models.fields.CharField')(default='/static/mtg.jpg', max_length=70, blank=True)),
            ('private_group', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('admin_id', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'placetoplay', ['Groups'])

        # Adding M2M table for field games_link on 'Groups'
        m2m_table_name = db.shorten_name(u'placetoplay_groups_games_link')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('groups', models.ForeignKey(orm[u'placetoplay.groups'], null=False)),
            ('games', models.ForeignKey(orm[u'placetoplay.games'], null=False))
        ))
        db.create_unique(m2m_table_name, ['groups_id', 'games_id'])

        # Adding model 'UserExtension'
        db.create_table(u'placetoplay_userextension', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_link', self.gf('django.db.models.fields.related.OneToOneField')(related_name='extension', unique=True, to=orm['auth.User'])),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('characteristics', self.gf('django.db.models.fields.TextField')(max_length=255, blank=True)),
            ('game_pref1', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('game_pref2', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('game_pref3', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('skill', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('facebook', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('image_path', self.gf('django.db.models.fields.CharField')(default='/static/mtg.jpg', max_length=100)),
        ))
        db.send_create_signal(u'placetoplay', ['UserExtension'])

        # Adding M2M table for field friends on 'UserExtension'
        m2m_table_name = db.shorten_name(u'placetoplay_userextension_friends')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_userextension', models.ForeignKey(orm[u'placetoplay.userextension'], null=False)),
            ('to_userextension', models.ForeignKey(orm[u'placetoplay.userextension'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_userextension_id', 'to_userextension_id'])

        # Adding M2M table for field group_link on 'UserExtension'
        m2m_table_name = db.shorten_name(u'placetoplay_userextension_group_link')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userextension', models.ForeignKey(orm[u'placetoplay.userextension'], null=False)),
            ('groups', models.ForeignKey(orm[u'placetoplay.groups'], null=False))
        ))
        db.create_unique(m2m_table_name, ['userextension_id', 'groups_id'])

        # Adding M2M table for field games_link on 'UserExtension'
        m2m_table_name = db.shorten_name(u'placetoplay_userextension_games_link')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userextension', models.ForeignKey(orm[u'placetoplay.userextension'], null=False)),
            ('games', models.ForeignKey(orm[u'placetoplay.games'], null=False))
        ))
        db.create_unique(m2m_table_name, ['userextension_id', 'games_id'])


    def backwards(self, orm):
        # Deleting model 'Games'
        db.delete_table(u'placetoplay_games')

        # Deleting model 'Groups'
        db.delete_table(u'placetoplay_groups')

        # Removing M2M table for field games_link on 'Groups'
        db.delete_table(db.shorten_name(u'placetoplay_groups_games_link'))

        # Deleting model 'UserExtension'
        db.delete_table(u'placetoplay_userextension')

        # Removing M2M table for field friends on 'UserExtension'
        db.delete_table(db.shorten_name(u'placetoplay_userextension_friends'))

        # Removing M2M table for field group_link on 'UserExtension'
        db.delete_table(db.shorten_name(u'placetoplay_userextension_group_link'))

        # Removing M2M table for field games_link on 'UserExtension'
        db.delete_table(db.shorten_name(u'placetoplay_userextension_games_link'))


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
            'amount_owned': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'category': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'comments': ('django.db.models.fields.TextField', [], {'default': "'FUCK SOUTH'"}),
            'date_published': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_path': ('django.db.models.fields.TextField', [], {'default': "'/static/mtg.jpeg'"}),
            'maker': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'mechanics': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'optimal_players': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'rating': ('django.db.models.fields.IntegerField', [], {})
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