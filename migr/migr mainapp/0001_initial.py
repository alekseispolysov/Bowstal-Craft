# Generated by Django 3.1.7 on 2021-07-07 10:41

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=30, null=True)),
                ('subject', models.CharField(max_length=50, null=True)),
                ('text', models.TextField(null=True)),
                ('date_sent', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('preview_text', models.CharField(blank=True, max_length=400, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('preview_picture', models.ImageField(blank=True, default='home_posts/sample_image.jpg', null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='SecurityEmailMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=30, null=True)),
                ('subject', models.CharField(max_length=50, null=True)),
                ('topic', models.CharField(choices=[('Bug on website', 'Bug on website'), ('Violation', 'Violation'), ('Suggestions', 'Suggestions'), ('Help', 'Help'), ('Bug on server', 'Bug on server'), ('Bug with plugins', 'Bug with plugins'), ('Other', 'Other')], max_length=100, null=True)),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('date_sent', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CommentToPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_comment_news', to='mainapp.post')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_comment_news', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]