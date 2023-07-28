# Generated by Django 4.2.1 on 2023-07-10 03:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('med_test1_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='med_test1_report',
            name='created_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='med_test1_report',
            name='t14_1',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='med_test1_report',
            name='t14_2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='med_test1_report',
            name='t14_3',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='med_test1_report',
            name='t14_4',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='med_test1_report',
            name='t15_1',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='med_test1_report',
            name='t15_2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='med_test1_report',
            name='t17',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='med_test1_report',
            name='t18',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='med_test1_report',
            name='t19',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='med_test1_report',
            name='t20',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='med_test1_report',
            name='t21',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='med_test1_report',
            name='t22',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='med_test1_report',
            name='t23',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='med_test1_report',
            name='t23_1',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='med_test1_report',
            name='t23_2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='med_test1_report',
            name='t23_3',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='med_test1_report',
            name='t23_4',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='med_test1_report',
            name='t23_5',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='med_test1_report',
            name='t24',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='med_test1_report',
            name='t24_1',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='med_test1_report',
            name='t24_2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='med_test1_report',
            name='t25',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='med_test1_report',
            name='t26',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='med_test1_report',
            name='t27',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='med_test1_report',
            name='t27_1',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='med_test1_report',
            name='t27_2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='med_test1_report',
            name='t27_3',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='med_test1_report',
            name='t27_4',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='med_test1_report',
            name='t27_5',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='med_test1_report',
            name='t27_6',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='med_test1_report',
            name='t28',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='med_test1_report',
            name='t28_1',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='med_test1_report',
            name='t28_2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='med_test1_report',
            name='t28_3',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='med_test1_report',
            name='t29',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='med_test1_report',
            name='t30',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='med_test1_report',
            name='t30_1',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='med_test1_report',
            name='t30_2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='med_test1_report',
            name='t31',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='med_test1_report',
            name='t31_1',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='med_test1_report',
            name='t31_2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='med_test1_report',
            name='t31_3',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='med_test1_report',
            name='t31_4',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='med_test1_report',
            name='t32',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='med_test1_report',
            name='t33',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='med_test1_report',
            name='t34',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='med_test1_report',
            name='t34_1',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='med_test1_report',
            name='t34_2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='med_test1_report',
            name='t35',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='med_test1_report',
            name='t35_1',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='med_test1_report',
            name='t35_2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='med_test1_report',
            name='t36',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='med_test1_report',
            name='t36_1',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='med_test1_report',
            name='t36_2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='med_test1_report',
            name='t36_3',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='med_test1_report',
            name='t37',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='med_test1_report',
            name='t38',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='med_test1_report',
            name='t39',
            field=models.CharField(max_length=200, null=True),
        ),
    ]