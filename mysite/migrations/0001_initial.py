# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestInline',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('content1', models.TextField()),
                ('content2', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TestPage',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('content1', models.TextField()),
                ('content2', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='testinline',
            name='page',
            field=models.ForeignKey(to='mysite.TestPage'),
        ),
    ]
