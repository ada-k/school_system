# Generated by Django 3.0.6 on 2020-05-29 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0002_auto_20200529_0814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='dob',
            field=models.IntegerField(blank=True),
        ),
    ]