# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0002_auto_20141116_2009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movement',
            name='balance',
        ),
    ]
