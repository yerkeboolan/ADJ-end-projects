# Generated by Django 2.1.1 on 2019-11-25 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20191105_1800'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='image_url',
            new_name='image',
        ),
    ]
