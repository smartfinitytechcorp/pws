# Generated by Django 3.1.13 on 2021-08-11 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('pwa', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slider',
            name='cmsplugin_ptr',
        ),
        migrations.DeleteModel(
            name='Slide',
        ),
        migrations.DeleteModel(
            name='Slider',
        ),
    ]
