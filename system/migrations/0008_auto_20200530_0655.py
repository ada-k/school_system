# Generated by Django 3.0.6 on 2020-05-30 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0007_auto_20200530_0627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='designation',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='full_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='job_group',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
