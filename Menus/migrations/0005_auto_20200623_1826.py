# Generated by Django 3.0.7 on 2020-06-23 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Menus', '0004_auto_20200623_1703'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='imgs',
            new_name='Image',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='names',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='positions',
            new_name='Position',
        ),
    ]
