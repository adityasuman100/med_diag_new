# Generated by Django 4.2.1 on 2023-07-11 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('med_test1_app', '0003_alter_med_test1_report_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='med_test1_report',
            name='lab_no',
            field=models.IntegerField(null=True),
        ),
    ]