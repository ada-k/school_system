# Generated by Django 3.0.6 on 2020-05-30 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0008_auto_20200530_0655'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]