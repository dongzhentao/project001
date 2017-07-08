# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uname', models.CharField(max_length=20)),
                ('upsd', models.CharField(max_length=40)),
                ('uphone', models.CharField(max_length=11)),
                ('umail', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Ushou',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('shouname', models.CharField(max_length=20)),
                ('shouphone', models.CharField(max_length=11)),
                ('shoupost', models.CharField(default=b'', max_length=6)),
                ('shouinfo', models.ForeignKey(to='userinfo.UserInfo')),
            ],
        ),
    ]
