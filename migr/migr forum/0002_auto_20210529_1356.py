# Generated by Django 3.1.7 on 2021-05-29 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commenttopost',
            old_name='text',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='forumpost',
            old_name='text',
            new_name='content',
        ),
    ]