# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20150702_1220'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndicatorToTrackedtime',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.PositiveSmallIntegerField(default=50)),
                ('indicator', models.ForeignKey(to='core.Indicator')),
                ('tracked_time', models.ForeignKey(to='core.TrackedTime')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='domain',
            options={'ordering': ['pk']},
        ),
        migrations.AlterModelOptions(
            name='indicator',
            options={'ordering': ['pk']},
        ),
        migrations.AddField(
            model_name='trackedtime',
            name='indicators',
            field=models.ManyToManyField(to='core.Indicator', through='core.IndicatorToTrackedtime'),
            preserve_default=True,
        ),
    ]
