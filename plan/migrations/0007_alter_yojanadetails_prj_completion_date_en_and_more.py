# Generated by Django 4.0.5 on 2022-07-10 02:38

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0006_rename_memberone_citizen_comitteemembers_member_citizen_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yojanadetails',
            name='prj_completion_date_en',
            field=models.DateField(default=datetime.datetime(2022, 7, 10, 2, 38, 29, 578371, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='yojanadetails',
            name='prj_start_date_en',
            field=models.DateField(default=datetime.datetime(2022, 7, 10, 2, 38, 29, 578371, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='Tippani',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_path', models.FileField(upload_to='files')),
                ('prj_ref', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='plan.yojanadetails')),
            ],
        ),
        migrations.CreateModel(
            name='Samjhauta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_path', models.FileField(upload_to='files')),
                ('prj_ref', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='plan.yojanadetails')),
            ],
        ),
        migrations.CreateModel(
            name='Karyadesh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_path', models.FileField(upload_to='files')),
                ('prj_ref', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='plan.yojanadetails')),
            ],
        ),
    ]
