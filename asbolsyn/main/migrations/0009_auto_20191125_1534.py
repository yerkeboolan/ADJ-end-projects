# Generated by Django 2.1.1 on 2019-11-25 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_menuitem_with_garnish'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ordermenuitem',
            options={'verbose_name': "Order's menu item", 'verbose_name_plural': "Order's menu items"},
        ),
        migrations.RenameField(
            model_name='businesscenter',
            old_name='image_url',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='menu',
            old_name='image_url',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='menuitem',
            old_name='image_url',
            new_name='image',
        ),
    ]
