# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('waffle', '0007_switch_all_sites_override'),
    ]

    operations = [
        migrations.AddField(
            model_name='sample',
            name='all_sites_override',
            field=models.BooleanField(
                default=True,
                help_text=b"When True this sample is used for all sites"
                          b" IMPORTANT: don't allow to create two samples with the same name"),
        )
    ]
