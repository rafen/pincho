# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('button', '0002_chairstate_acc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Temp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('temp', models.IntegerField(default=0, null=True, blank=True)),
                ('humidity', models.IntegerField(default=0, null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
