# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(null=True, blank=True)),
                ('picture', models.ImageField(upload_to=b'mysite/static/char_images', blank=True)),
                ('name', models.CharField(unique=True, max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, unique=True, null=True, verbose_name=b'Title')),
                ('author', models.CharField(max_length=50, null=True, verbose_name=b'Author')),
                ('series', models.CharField(max_length=100, null=True, verbose_name=b'Series', blank=True)),
                ('picture', models.ImageField(null=True, upload_to=b'mysite/static/book_images', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('votes', models.IntegerField(null=True, verbose_name=b'Votes', blank=True)),
                ('actors', models.ManyToManyField(related_query_name=b'character', to='shelf.Actor', null=True, db_table=b'character_actor_relation', blank=True)),
                ('books', models.ManyToManyField(related_query_name=b'character', to='shelf.Book', null=True, db_table=b'character_book_relation', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(max_length=50, verbose_name=b'User')),
                ('created_on', models.DateTimeField(auto_now=True, verbose_name=b'Comment Updated')),
                ('text', models.CharField(max_length=2000, verbose_name=b'Comment Text', blank=True)),
                ('character', models.ForeignKey(blank=True, to='shelf.Character', null=True)),
                ('parent', models.ForeignKey(blank=True, to='shelf.Comment', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
