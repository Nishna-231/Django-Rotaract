# Generated by Django 3.0.7 on 2020-06-23 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Menus', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='team',
            options={'verbose_name_plural': 'Team'},
        ),
        migrations.RenameField(
            model_name='event',
            old_name='event_name',
            new_name='Name',
        ),
    ]
