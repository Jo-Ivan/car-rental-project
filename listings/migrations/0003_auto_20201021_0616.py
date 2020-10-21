# Generated by Django 3.1.2 on 2020-10-21 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20201021_0615'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='city',
            new_name='borough',
        ),
        migrations.RenameField(
            model_name='listing',
            old_name='address',
            new_name='car',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='bathrooms',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='bedrooms',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='garage',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='lot_size',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='photo_4',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='photo_5',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='photo_6',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='sqft',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='state',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='zipcode',
        ),
        migrations.AddField(
            model_name='listing',
            name='is_rented',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_1',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_2',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_3',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_main',
            field=models.ImageField(upload_to='photos/%Y/%m/%d'),
        ),
    ]