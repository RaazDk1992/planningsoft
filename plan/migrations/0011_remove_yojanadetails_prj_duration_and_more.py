# Generated by Django 4.0.5 on 2022-07-09 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0010_woda_yojanadetails_area_ref'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='yojanadetails',
            name='prj_duration',
        ),
        migrations.AddField(
            model_name='yojanadetails',
            name='is_multiyear',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='yojanadetails',
            name='prj_completion_date',
            field=models.CharField(default='null', max_length=80),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='yojanadetails',
            name='prj_completion_date_en',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='yojanadetails',
            name='prj_start_date',
            field=models.CharField(default='null', max_length=80),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='yojanadetails',
            name='prj_start_date_en',
            field=models.DateField(auto_now=True),
        ),
    ]
