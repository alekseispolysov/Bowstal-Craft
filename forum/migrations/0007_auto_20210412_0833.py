# Generated by Django 3.1.7 on 2021-04-12 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0006_auto_20210412_0824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forumpost',
            name='topic',
            field=models.CharField(choices=[('Important', 'Important'), ('Suggestions', 'Suggestions'), ('Help', 'Help'), ('Discussion', 'Discussion'), ('Other', 'Other')], max_length=100, null=True),
        ),
    ]