# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20141216_1956'),
        ('shelf', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='userprofile',
            field=models.ForeignKey(related_query_name=b'character', blank=True, to='account.UserProfile', null=True),
            preserve_default=True,
        ),
    ]
