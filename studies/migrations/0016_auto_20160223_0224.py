# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-23 02:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studies', '0015_auto_20160210_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datarequest',
            name='source',
            field=models.CharField(choices=[(b'american_gut', b'American Gut'), (b'go_viral', b'GoViral'), (b'pgp', b'Harvard Personal Genome Project'), (b'wildlife', b'Wild Life of Our Homes'), (b'data_selfie', b'Data selfie'), (b'runkeeper', b'RunKeeper'), (b'twenty_three_and_me', b'23andMe'), (b'ancestry_dna', b'AncestryDNA')], max_length=32),
        ),
    ]