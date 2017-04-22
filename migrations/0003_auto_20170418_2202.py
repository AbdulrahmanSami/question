# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0002_auto_20170418_1843'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Question_sessions',
            new_name='QuestionSession',
        ),
    ]
