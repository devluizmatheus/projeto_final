# Generated by Django 4.2.17 on 2024-12-11 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enjoyer',
            old_name='first_name',
            new_name='primeiro_nome',
        ),
        migrations.RenameField(
            model_name='enjoyer',
            old_name='last_name',
            new_name='sobrenome',
        ),
    ]
