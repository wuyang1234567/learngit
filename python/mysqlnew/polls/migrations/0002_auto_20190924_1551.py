# Generated by Django 2.2.5 on 2019-09-24 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='email',
            new_name='emails',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='password',
            new_name='passwords',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='time',
            new_name='times',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='username',
            new_name='usernames',
        ),
    ]
