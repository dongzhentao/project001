# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0002_auto_20170705_2154'),
    ]

    operations = [
        migrations.AddField(
            model_name='ushou',
            name='shouaddress',
            field=models.CharField(default=b'', max_length=100),
        ),
    ]
