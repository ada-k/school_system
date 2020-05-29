# Generated by Django 3.0.6 on 2020-05-29 08:33

from django.db import migrations, models
import partial_date.fields


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0005_auto_20200529_0828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='name',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='ground_inventory',
            name='area_to_repair',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ground_inventory',
            name='description',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='ground_inventory',
            name='ground_type',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='ground_inventory',
            name='remarks',
            field=models.TextField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='ground_inventory',
            name='total_area',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ground_inventory',
            name='total_surface_area',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ground_inventory',
            name='unused_area',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='contact',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id_no',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='location',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='contact',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='designation',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='dob',
            field=partial_date.fields.PartialDateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='dofa',
            field=partial_date.fields.PartialDateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='email',
            field=models.EmailField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='full_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='gender',
            field=models.CharField(blank=True, choices=[('F', 'FEMALE'), ('M', 'MALE'), ('I', 'INTERSEX')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='id_no',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='job_group',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='kra_pin',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='tsc_no',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='structure_inventory',
            name='description',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='structure_inventory',
            name='quantity_to_repair',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='structure_inventory',
            name='quantity_to_replace',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='structure_inventory',
            name='remarks',
            field=models.TextField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='structure_inventory',
            name='struct_type',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='structure_inventory',
            name='total_quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='structure_inventory',
            name='total_surface_area',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='structure_inventory',
            name='unused_quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='adm_date',
            field=partial_date.fields.PartialDateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='adm_no',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='border_or_day',
            field=models.CharField(blank=True, choices=[('D', 'DAY'), ('B', 'BORDER')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='class_on_adm_day',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='dob',
            field=partial_date.fields.PartialDateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='excempted_from_religious_instr',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='full_name',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(blank=True, choices=[('F', 'FEMALE'), ('M', 'MALE'), ('I', 'INTERSEX')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='guardian_name',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='home_address',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_school',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='leaving_cert_no',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='leaving_date',
            field=partial_date.fields.PartialDateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='remarks',
            field=models.TextField(blank=True, max_length=40, null=True),
        ),
    ]
