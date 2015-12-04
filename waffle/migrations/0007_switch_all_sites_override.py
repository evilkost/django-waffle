# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('waffle', '0006_auto_20150923_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='switch',
            name='all_sites_override',
            field=models.BooleanField(default=True, help_text=b'When True this switch is used for all sites'),
        ),
    ]
