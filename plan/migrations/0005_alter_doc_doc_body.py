# Generated by Django 4.0.5 on 2022-07-09 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0004_doc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doc',
            name='doc_body',
            field=models.TextField(max_length=2000),
        ),
    ]
