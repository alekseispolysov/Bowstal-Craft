# Generated by Django 3.1.7 on 2021-04-12 06:24

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_auto_20210411_0842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forumpost',
            name='text',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AlterField(
            model_name='forumpost',
            name='topic',
            field=models.CharField(max_length=100, null=True),
        ),
    ]