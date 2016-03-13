# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-07 22:52
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations


def update_slugs(apps, schema_editor):
    DataRequestProject = apps.get_model('private_sharing',
                                        'DataRequestProject')

    for project in DataRequestProject.objects.all():
        project.name = project.name + ''
        project.save()

    for project in DataRequestProject.objects.all():
        print project.slug


class Migration(migrations.Migration):

    dependencies = [
        ('private_sharing', '0016_auto_20160304_0655'),
    ]

    operations = [
        # create with unique=False
        migrations.AddField(
            model_name='datarequestproject',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='', editable=False, populate_from='name', unique=False),
            preserve_default=False,
        ),

        # update all slugs
        migrations.RunPython(update_slugs),

        # continued in next migration
    ]