# Generated by Django 4.0.5 on 2022-07-23 13:52

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import plan.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BudgetType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comittee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comittee_name', models.CharField(max_length=200)),
                ('comittee_name_en', models.CharField(max_length=200)),
                ('comittee_address', models.CharField(max_length=100)),
                ('black_listed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=100)),
                ('designation_en', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Doc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_ref', models.CharField(max_length=20)),
                ('doc_name', models.CharField(max_length=100)),
                ('doc_body', models.TextField(max_length=2000)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='FY',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fy', models.CharField(max_length=30)),
                ('fy_np', models.CharField(max_length=30)),
                ('isactive', models.BooleanField(default=True)),
            ],
            options={
                'unique_together': {('fy', 'fy_np', 'isactive')},
            },
        ),
        migrations.CreateModel(
            name='MajorSector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(max_length=30)),
                ('section_en', models.CharField(max_length=30)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('officeName', models.CharField(max_length=200)),
                ('officeAddress', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('type_en', models.CharField(max_length=100)),
                ('isActive', models.BooleanField(default=True)),
                ('sector_ref', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='plan.majorsector')),
            ],
        ),
        migrations.CreateModel(
            name='ResponsibleGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_type', models.CharField(max_length=100)),
                ('group_type_en', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TypeOfProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_description', models.CharField(max_length=40)),
                ('type_description_en', models.CharField(max_length=40)),
                ('isActive', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='UnitOfWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_name', models.CharField(max_length=20)),
                ('unit_name_en', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ward', models.CharField(max_length=10)),
                ('ward_en', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Woda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('woda', models.CharField(max_length=3)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='YojanaType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='YojanaDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prj_ref', models.CharField(max_length=40)),
                ('prj_name', models.CharField(max_length=100)),
                ('prj_tole', models.CharField(max_length=50)),
                ('prj_start_date', models.CharField(max_length=80)),
                ('prj_start_date_en', models.DateField(default=datetime.datetime(2022, 7, 23, 13, 52, 42, 247172, tzinfo=utc))),
                ('prj_completion_date', models.CharField(max_length=80)),
                ('prj_completion_date_en', models.DateField(default=datetime.datetime(2022, 7, 23, 13, 52, 42, 247172, tzinfo=utc))),
                ('is_multiyear', models.BooleanField(default=False)),
                ('amount_of_work', models.FloatField(default=0.0)),
                ('amt_from_palika', models.CharField(default='००', max_length=5)),
                ('amt_from_palika_en', models.FloatField(default=0.0)),
                ('amt_from_comittee', models.CharField(default='००', max_length=5)),
                ('amt_from_comittee_en', models.FloatField(default=0.0)),
                ('amt_from_gai_sasa', models.CharField(default='००', max_length=5)),
                ('amt_from_gai_sasa_en', models.FloatField(default=0.0)),
                ('prj_estimate', models.CharField(default='००', max_length=5)),
                ('prj_estimate_en', models.FloatField(default=0.0)),
                ('estimate_in_letters', models.CharField(max_length=100)),
                ('affected_household', models.CharField(default='००', max_length=5)),
                ('affected_household_en', models.FloatField(default=0.0)),
                ('affected_community', models.CharField(default='००', max_length=5)),
                ('affected_community_en', models.IntegerField(default=0)),
                ('affected_people', models.CharField(default='००', max_length=5)),
                ('affected_people_en', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('is_complete', models.BooleanField(default=False)),
                ('time_stamp', models.DateTimeField(auto_now=True)),
                ('area_ref', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='plan.woda')),
                ('budget_type', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='plan.budgettype')),
                ('fy_ref', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='plan.fy')),
                ('plan_type', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='plan.yojanatype')),
                ('prj_type', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='plan.projecttype')),
                ('sector_ref', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='plan.majorsector')),
                ('type_prj_ref', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='plan.typeofproject')),
                ('unit_of_work', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='plan.unitofwork')),
            ],
        ),
        migrations.CreateModel(
            name='Tippani',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('file_path', models.FileField(upload_to='files')),
                ('prj_ref', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='plan.yojanadetails')),
            ],
        ),
        migrations.CreateModel(
            name='Samjhauta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('file_path', models.FileField(upload_to='files')),
                ('prj_ref', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='plan.yojanadetails')),
            ],
        ),
        migrations.CreateModel(
            name='relmap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offRef', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='plan.office')),
                ('uRef', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProgressGeneral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('population', models.IntegerField()),
                ('amt', models.FloatField()),
                ('remarks', models.TextField(max_length=200)),
                ('sector_ref', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='plan.majorsector')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sanketNo', models.CharField(blank=True, max_length=30)),
                ('contactNo', models.CharField(blank=True, max_length=13)),
                ('is_active', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Karyadesh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('file_path', models.FileField(upload_to='files')),
                ('prj_ref', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='plan.yojanadetails')),
            ],
        ),
        migrations.CreateModel(
            name='Finalize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_date', models.CharField(max_length=50)),
                ('message', models.TextField(max_length=200)),
                ('baseString', models.TextField(max_length=500)),
                ('similarity', models.FloatField(default=0.0)),
                ('prj_ref', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='plan.yojanadetails')),
            ],
        ),
        migrations.CreateModel(
            name='count',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('count_np', models.CharField(max_length=10)),
                ('fy_ref', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='plan.fy')),
            ],
        ),
        migrations.CreateModel(
            name='ComitteeMembers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_name', models.CharField(max_length=50)),
                ('member_citizen', models.CharField(max_length=50)),
                ('member_citizen_img', models.ImageField(default='default.jpg', upload_to=plan.models.comitteemembers_citizen_file_path)),
                ('member_image', models.ImageField(default='default.jpg', upload_to=plan.models.comitteemembers_citizen_file_path)),
                ('member_phone', models.CharField(max_length=12)),
                ('comittee_ref', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='plan.comittee')),
                ('member_designation', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='plan.designation')),
                ('project_ref', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='plan.yojanadetails')),
            ],
        ),
        migrations.AddField(
            model_name='comittee',
            name='project_ref',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='plan.yojanadetails'),
        ),
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0.0)),
                ('is_active', models.BooleanField(default=True)),
                ('budget_type', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='plan.budgettype')),
                ('fy_ref', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='plan.fy')),
                ('plan_type', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='plan.yojanatype')),
            ],
        ),
    ]
