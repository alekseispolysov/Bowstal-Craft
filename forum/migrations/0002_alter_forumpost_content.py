# Generated by Django 4.2.16 on 2024-11-10 08:25

from django.db import migrations
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forumpost',
            name='content',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True),
        ),
    ]
