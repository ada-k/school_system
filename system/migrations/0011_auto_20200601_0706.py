# Generated by Django 3.0.6 on 2020-06-01 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0010_auto_20200601_0645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='adm_no',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
