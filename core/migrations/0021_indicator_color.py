# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_auto_20150702_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='indicator',
            name='color',
            field=models.CharField(default=b'95CEFF', max_length=6),
            preserve_default=True,
        ),
    ]
