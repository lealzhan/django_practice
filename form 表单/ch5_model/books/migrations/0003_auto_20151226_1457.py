# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_database_test'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='database_test',
            new_name='DatabaseTest',
        ),
    ]
