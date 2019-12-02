# Generated by Django 2.1.1 on 2019-12-01 06:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_courierprofile_restaurantadminprofile_staffprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courierprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='couriers', to=settings.AUTH_USER_MODEL),
        ),
    ]