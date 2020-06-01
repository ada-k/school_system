# Generated by Django 3.0.6 on 2020-06-01 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0012_auto_20200601_0710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ground_inventory',
            name='item_no',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='id_no',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='tsc_no',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='structure_inventory',
            name='item_no',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='adm_no',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]