# Generated by Django 4.0.5 on 2022-07-09 15:21

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0003_yojanadetails_estimate_in_letters_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comittee',
            name='project_ref',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.RESTRICT, to='plan.yojanadetails'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='yojanadetails',
            name='prj_completion_date_en',
            field=models.DateField(default=datetime.datetime(2022, 7, 9, 15, 21, 31, 975703, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='yojanadetails',
            name='prj_start_date_en',
            field=models.DateField(default=datetime.datetime(2022, 7, 9, 15, 21, 31, 975703, tzinfo=utc)),
        ),
    ]
